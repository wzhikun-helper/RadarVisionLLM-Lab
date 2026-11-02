"""Check published reading entrypoints and CSV structure using only the standard library.

This is distinct from validate_lab.py: historical audit links and unpublished local
assets are not public entrypoints. No HTTP requests, model runs or file writes.
"""
from pathlib import Path
from urllib.parse import unquote
import argparse
import csv
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_MD = [
    'README.md', 'CONTRIBUTING.md', 'NOTICE.md', 'paper_notes/README.md',
    'papers/README.md', 'docs/README.md', 'figures/README.md',
    'reproductions/README.md', 'paper_notes/P001_论文精读.md',
    'paper_notes/P001_概念查询宝典.md', 'paper_notes/P002_CRN.md',
    'paper_notes/P002_概念查询宝典.md',
    'docs/research_gaps/P002_CRN_Limitations_Research_Gap.md',
    'docs/innovation_bank/P002_CRN_INNOVATION_NOTES.md',
    'docs/research_log/P002_CRN_READING_REPORT.md',
    'reproductions/P002_CRN/README.md', 'figures/library/P002/FIGURE_INDEX.md',
    'paper_notes/templates/paper_archive_checklist.md',
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--include-untracked', action='store_true',
                        help='Preview pending documents before staging; not a publication claim.')
    args = parser.parse_args()
    command = ['git', 'ls-files', '-z']
    published = set(subprocess.check_output(command, cwd=ROOT).decode('utf-8').split('\0')) - {''}
    if args.include_untracked:
        other = subprocess.check_output(
            ['git', 'ls-files', '--others', '--exclude-standard', '-z'], cwd=ROOT)
        published.update(other.decode('utf-8').split('\0'))
    errors = []
    links = 0
    for key in PUBLIC_MD:
        p = ROOT / key
        if key not in published or not p.is_file():
            errors.append({'missing_published_document': key})
            continue
        text = p.read_text(encoding='utf-8-sig')
        text = re.sub(r'```.*?```|~~~.*?~~~', '', text, flags=re.S)
        if '![[ ' in text or re.search(r'!\[\[', text):
            errors.append({'obsidian_only_embed': key})
        for url in re.findall(r'!?\[[^\]\n]*\]\(([^\n]*?)\)', text):
            url = re.sub(r'\s+"[^"]*"$', '', url.strip()).strip('<>')
            if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:', url):
                continue
            target = unquote(url.split('#', 1)[0])
            q = (p.parent / target).resolve() if target else p
            try:
                relative = q.relative_to(ROOT).as_posix()
            except ValueError:
                errors.append({'path_outside_repository': {'document': key, 'target': url}})
                continue
            if not q.exists() or (q.is_file() and relative not in published):
                errors.append({'unpublished_link': {'document': key, 'target': url}})
            else:
                links += 1
    columns = {}
    for key in sorted(published):
        if not key.endswith('.csv') or not (ROOT / key).is_file():
            continue
        with (ROOT / key).open(encoding='utf-8-sig', newline='') as stream:
            rows = list(csv.reader(stream))
        if not rows or any(len(row) != len(rows[0]) for row in rows):
            errors.append({'invalid_csv_width': key})
            continue
        columns[key] = len(rows[0])
    for key, width in [('papers/paper_matrix.csv', 36)]:
        if columns.get(key) != width:
            errors.append({'unexpected_schema': key, 'expected_columns': width})
    print(json.dumps({'passed': not errors, 'errors': errors,
                      'documents_checked': len(PUBLIC_MD), 'local_links_checked': links,
                      'csv_columns': columns, 'preview_includes_untracked': args.include_untracked,
                      'scope': 'Published reading entrypoints and CSV row widths; no HTTP, historical-asset or model verification.'},
                     ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
