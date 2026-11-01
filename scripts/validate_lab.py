"""Read-only validation of the current registered research notes and non-PPT resource library."""
from pathlib import Path
import argparse,csv,hashlib,json,re,sys,zipfile
from urllib.parse import unquote
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

def status_table(record):
    """Render the root README summary from the sole current status source."""
    lines=['| 编号 / 论文 | 阅读状态 | 验收证据 | 工程状态 |',
           '| --- | --- | --- | --- |']
    for paper in record['papers']:
        lines.append(f"| [{paper['id']} · {paper['title']}]({paper['entry']}) | {paper['reading']} | {paper['review']} | {paper['code']} |")
    return '\n'.join(lines)


def validate_tracked(root, destination=None, include_untracked=False):
    """Check an explicitly declared Git/document scope, not private asset hashes."""
    import subprocess,posixpath
    def git_paths(*args):
        data=subprocess.check_output(['git',*args,'-z'],cwd=root).decode('utf-8')
        return set(data.split('\0'))-{''}
    paths=git_paths('ls-files')
    if include_untracked:
        paths.update(git_paths('ls-files','--others','--exclude-standard'))
    errors=[];warnings=[];links=obsidian=json_count=yaml_count=python_count=0;columns={}
    fingerprints={};large=[];yaml_unchecked=[]
    sensitive_name=re.compile(r'(^|/)(\.env(?:\..*)?|id_rsa|id_ed25519|credentials(?:\..*)?|secrets?\.(?:json|ya?ml)|.*\.(?:pem|key|p12|pfx))$',re.I)
    token_patterns=[re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
                    re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{50,})\b'),
                    re.compile(r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b'),
                    re.compile(r'\bsk-(?:proj-)?[A-Za-z0-9_-]{36,}\b')]
    def present(target):
        return target in paths or any(x.startswith(target.rstrip('/')+'/') for x in paths)
    for key in sorted(paths):
        p=root/key
        if not p.is_file():
            errors.append({'missing_scoped_file':key});continue
        if sensitive_name.search(key) and not key.endswith('.env.example'):
            errors.append({'sensitive_path':key});continue
        if p.stat().st_size>=10*1024*1024:large.append({'path':key,'bytes':p.stat().st_size})
        if p.suffix.lower() in {'.pth','.pt','.ckpt','.onnx','.safetensors','.npy','.npz','.pkl','.bin'} or key.startswith(('data/raw/','data/datasets/','data/downloads/')):
            errors.append({'dataset_or_weight_in_scope':key})
        data=p.read_bytes()
        if len(data)<2_000_000 and p.suffix.lower() in {'.md','.py','.json','.csv','.yaml','.yml','.txt','.js','.mjs','.ps1','.sh'}:
            text=data.decode('utf-8-sig',errors='replace')
            if any(pattern.search(text) for pattern in token_patterns):errors.append({'potential_secret_value_redacted':key})
        if p.suffix=='.json':
            try:json.loads(data.decode('utf-8-sig'));json_count+=1
            except (ValueError,UnicodeError):errors.append({'invalid_json':key})
        if p.suffix.lower() in {'.yaml','.yml'}:
            try:
                import yaml
            except ImportError:yaml_unchecked.append(key)
            else:
                try:yaml.safe_load(data.decode('utf-8-sig'));yaml_count+=1
                except yaml.YAMLError:errors.append({'invalid_yaml':key})
        if p.suffix=='.py':
            try:compile(data.decode('utf-8-sig'),key,'exec');python_count+=1
            except (SyntaxError,UnicodeError):errors.append({'invalid_python':key})
        if p.suffix=='.csv':
            with p.open(encoding='utf-8-sig',newline='') as f:rows=list(csv.reader(f))
            if not rows or any(len(row)!=len(rows[0]) for row in rows):errors.append({'invalid_csv_width':key})
            else:columns[key]=len(rows[0])
            if key=='papers/paper_matrix.csv':
                ids=[row[0] for row in rows[1:]]
                if len(ids)!=len(set(ids)) or set(ids)!={'P001','P002','P003','P004'}:errors.append({'invalid_paper_ids':key})
        if p.suffix!='.md':continue
        prose=markdown_prose(data.decode('utf-8-sig'))
        for url in re.findall(r'!?\[[^\]\n]*\]\(([^\n]*?)\)',prose):
            url=re.sub(r'\s+"[^"]*"$','',url.strip()).strip('<>')
            if re.match(r'^(https?:|mailto:|app:|data:|codex:)',url):continue
            target=posixpath.normpath(posixpath.join(posixpath.dirname(key),unquote(url.split('#')[0])))
            if not present(target):errors.append({'missing_git_link_target':{'source':key,'target':url}})
            else:links+=1
        for url in re.findall(r'!?\[\[([^\]]+)\]\]',prose):
            name=unquote(url.split('|')[0].split('#')[0]);obsidian+=1
            if not name:continue
            candidates=[posixpath.normpath(posixpath.join(posixpath.dirname(key),name)),name,
                        posixpath.normpath(posixpath.join(posixpath.dirname(key),name+'.md')),name+'.md']
            if not any(present(x) for x in candidates):
                matches=[x for x in paths if Path(x).name==Path(name).name]
                if len(matches)!=1:errors.append({'unresolved_obsidian_target':{'source':key,'target':url}})
    if columns.get('papers/paper_matrix.csv')!=36 or columns.get('papers/paper_matrix_P001_import.csv')!=23:
        errors.append({'matrix_column_contract':columns})
    if columns.get('docs/innovation_bank/P001_ideas.csv')!=10 or columns.get('docs/innovation_bank/P002_ideas.csv')!=10:
        errors.append({'idea_column_contract':columns})
    status_key='docs/maintenance/RESEARCH_STATUS.json'
    if status_key not in paths:errors.append({'missing_current_status_source':status_key})
    else:
        status=json.loads((root/status_key).read_text(encoding='utf-8'))
        if [x['id'] for x in status['papers']]!=['P001','P002','P003','P004']:errors.append({'status_id_order':'P001-P004'})
        if [x['title'] for x in status['papers']][2:]!=['R4Det','MSSF']:errors.append({'status_p003_p004_identity':'R4Det/MSSF'})
        for paper in status['papers']:
            for target in [paper['entry']]+paper['evidence']+paper['canonical_notes']:
                if not present(target):errors.append({'status_target_missing':target})
        readme=(root/'README.md').read_text(encoding='utf-8')
        match=re.search(r'<!-- BEGIN RESEARCH STATUS -->\s*\n(.*?)\n<!-- END RESEARCH STATUS -->',readme,re.S)
        if not match or match[1].strip()!=status_table(status):errors.append({'readme_status_drift':'Update JSON and generated README table together; no automatic scientific status changes.'})
        if not present(status['baseline']['source']):errors.append({'baseline_evidence_missing':status['baseline']['source']})
    required=['docs/maintenance/REPOSITORY_GUIDE.md','docs/RESEARCH_WORKFLOW.md','papers/P001_PointPillars_VoD/README.md','papers/P002_CRN/README.md','papers/P003_R4Det/01_pre_readiness.md','reproductions/RECORDING_STANDARD.md']
    for key in required:
        if key not in paths:errors.append({'missing_important_entry':key})
    probes=['.env','.env.local','private.pem','credentials.json','data/raw/check.bin','checkpoints/check.pth','weights/check.safetensors']
    ignored=subprocess.run(['git','check-ignore','--no-index','--stdin','-z'],cwd=root,input=('\0'.join(probes)+'\0').encode('utf-8'),capture_output=True)
    if ignored.returncode not in (0,1):errors.append({'ignore_probe_error':ignored.returncode})
    covered=set(ignored.stdout.decode('utf-8').split('\0'))-{''}
    for probe in probes:
        if probe not in covered:errors.append({'missing_ignore_protection':probe})
    if yaml_unchecked:warnings.append({'yaml_not_parsed_missing_optional_dependency':yaml_unchecked})
    if large:warnings.append({'large_files_need_review':large})
    report={'passed':not errors,'scope':'tracked_plus_untracked_preview' if include_untracked else 'git_tracked_worktree_documents',
            'errors':errors,'warnings':warnings,'files_checked':len(paths),'markdown_local_targets':links,
            'obsidian_targets':obsidian,'json_parsed':json_count,'yaml_parsed':yaml_count,'yaml_unchecked':yaml_unchecked,
            'csv_columns':columns,'python_compiled':python_count,'ignore_probes':probes,'large_files':large,
            'claim_boundary':'Document/format/status/ignore checks only. Does not verify unpublished local assets, historical raw-byte hashes, external URLs, every anchor, all secrets, scientific mastery, model execution or reproduction. Use full scope on the complete local maintenance copy.'}
    emit_report(report,destination)
    return 0 if report['passed'] else 1

def main():
    global ROOT
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--report')
    ap.add_argument('--scope',choices=['full','tracked'],default='full',help='Full retains the original asset/hash rules; tracked checks explicit Git document scope.')
    ap.add_argument('--root',help='Read-only validation root; defaults to this checkout.')
    ap.add_argument('--include-untracked',action='store_true',help='Tracked-scope preview only; not proof of publication.')
    args=ap.parse_args()
    if args.root:ROOT=Path(args.root).resolve()
    if args.scope=='tracked':return validate_tracked(ROOT,args.report,args.include_untracked)
    if args.include_untracked:ap.error('--include-untracked requires --scope tracked')
    from pypdf import PdfReader
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
