"""Read-only validation of the current registered research notes and non-PPT resource library."""
from pathlib import Path
import argparse,csv,hashlib,json,re,sys,zipfile
from urllib.parse import unquote
from pypdf import PdfReader
from maintenance_paths import ROOT,emit_report

def sha(data):return hashlib.sha256(data).hexdigest()
def markdown_prose(text):
    """Return prose only, respecting nested shorter fences in historical snapshots."""
    output=[];fence=None
    for line in text.splitlines():
        match=re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$',line)
        if fence:
            if match and match[1][0]==fence[0] and len(match[1])>=fence[1] and not match[2].strip():
                fence=None
            continue
        if match:
            fence=(match[1][0],len(match[1]));continue
        output.append(line)
    return '\n'.join(output)
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--report');args=ap.parse_args()
    record=json.loads((ROOT/'docs/maintenance/P001_CURRENT_STATE.json').read_text(encoding='utf-8'))
    assert record['status']=='completed'
    errors=[];pdfs=[];history=0;links=0
    for key,expected in record['expected_files'].items():
        p=ROOT/key
        if not p.is_file() or sha(p.read_bytes())!=expected['sha256']:
            errors.append({'retained_resource_missing_or_changed':key})
    for item in record['deletions']:
        if (ROOT/item['path']).exists():errors.append({'retired_file_reappeared':item['path']})
    for item in record['packed_p001_history']:
        if (ROOT/item['source']).exists():errors.append({'unpacked_history_reappeared':item['source']})
        with zipfile.ZipFile(ROOT/item['archive']) as z:
            data=z.read(item['entry'])
        if len(data)!=item['bytes'] or sha(data)!=item['sha256']:errors.append({'historical_archive_changed':item['source']})
        history+=1
    for item in record['replacements']:
        p=ROOT/item['destination'];data=p.read_bytes()
        assert sha(data)==item['sha256']
        if p.suffix.lower()=='.pdf':
            assert len(PdfReader(p).pages)==item['pages']
        else:
            for embed in re.findall(r'!\[\[([^\]]+)\]\]',data.decode('utf-8-sig')):
                if not (p.parent/embed.split('|')[0]).is_file():errors.append({'missing_note_embed':embed})
        pdfs.append({'file':item['destination'],'sha256':sha(data)})
    columns={};compiled=0
    for p in ROOT.rglob('*'):
        if not p.is_file() or '.git' in p.relative_to(ROOT).parts:continue
        key=p.relative_to(ROOT).as_posix()
        if p.suffix.lower() in {'.ppt','.pptx','.pptm','.pps','.ppsx','.ppsm'}:errors.append({'unexpected_presentation':key})
        if any('p002' in part.lower() for part in p.relative_to(ROOT).parts) and key not in record.get('registered_p002_assets',[]):errors.append({'unexpected_removed_project_file':key})
        if p.suffix=='.csv':
            with p.open(encoding='utf-8-sig',newline='') as f:rows=list(csv.reader(f))
            assert rows and all(len(x)==len(rows[0]) for x in rows);columns[key]=len(rows[0])
            if key=='papers/paper_matrix.csv':
                ids=[x[0] for x in rows[1:]]
                assert len(ids)==len(set(ids)) and set(ids)==set(record['organization_20261030']['approved_matrix_ids'])
        if p.suffix=='.py' and not key.startswith('archive/'):
            compile(p.read_text(encoding='utf-8-sig'),key,'exec');compiled+=1
        if p.suffix!='.md':continue
        text=markdown_prose(p.read_text(encoding='utf-8-sig'))
        for url in re.findall(r'!?\[[^\]\n]*\]\(([^\n]*?)\)',text):
            url=re.sub(r'\s+"[^"]*"$','',url.strip()).strip('<>')
            if re.match(r'^(https?:|mailto:|app:|data:|codex:)',url):continue
            target=unquote(url.split('#')[0]);q=(p.parent/target).resolve()
            if not q.exists():errors.append({'broken_link':{'source':key,'target':url}})
            else:links+=1
    assert columns['papers/paper_matrix.csv']==36 and columns['papers/paper_matrix_P001_import.csv']==23
    report={'passed':not errors,'errors':errors,'formal_p001_notes':pdfs,'presentation_files_expected':0,'historical_entries_verified':history,'retained_files_verified':len(record['expected_files']),'csv_columns':columns,'existing_markdown_targets':links,'python_files_compiled':compiled,'claim_boundary':'Checks retained P001 bytes, source PDF copies, packed historical bytes and links. No PPT generation, training or evaluation.'}
    emit_report(report,args.report);return 0 if report['passed'] else 1
if __name__=='__main__':sys.exit(main())
