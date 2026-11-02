"""Read-only structural checks shared by P001 and P002; not historical or model validation."""
from pathlib import Path
from urllib.parse import unquote
import argparse
import csv
import json
import re
import sys
from maintenance_paths import ROOT, emit_report


def markdown_prose(text):
    output = []
    fence = None
    for line in text.splitlines():
        match = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= fence[1] and not match[2].strip():
                fence = None
            continue
        if match:
            fence = (match[1][0], len(match[1]))
            continue
        output.append(line)
    return '\n'.join(output)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report')
    args = parser.parse_args()
    errors = []
    archives = {}
    for pid, stem, review, concepts, innovation in [
        ('P001', 'PointPillars_VoD', 'P001_论文精读.md', 'P001_概念查询宝典.md', 'P001_INNOVATION_NOTES.md'),
        ('P002', 'CRN', 'P002_CRN.md', 'P002_概念查询宝典.md', 'P002_CRN_INNOVATION_NOTES.md'),
    ]:
        suffix = '' if pid == 'P001' else '_CRN'
        roles = {
            'review': f'paper_notes/{review}',
            'concepts': f'paper_notes/{concepts}',
            'assets': f'paper_notes/assets/{pid}' + ('' if pid == 'P001' else '_CRN'),
            'figures': f'figures/library/{pid}/FIGURE_INDEX.md',
            'gaps': f'docs/research_gaps/{pid}{suffix}_Limitations_Research_Gap.md',
            'innovation': f'docs/innovation_bank/{innovation}',
            'ideas': f'docs/innovation_bank/{pid}_ideas.csv',
            'reading_log': f'docs/research_log/{pid}{suffix}_READING_REPORT.md',
            'feedback': f'docs/research_log/{pid}{suffix}_REVIEW.md',
            'reproduction': f'reproductions/{pid}_{stem}/README.md',
            'experiments': f'reproductions/{pid}_{stem}/experiment_tracker.csv',
            'registration': 'papers/paper_matrix.csv',
        }
        archives[pid] = roles
        for role, key in roles.items():
            p = ROOT / key
            if role == 'assets':
                valid = p.is_dir() and any(x.is_file() for x in p.iterdir())
            else:
                valid = p.is_file() and p.stat().st_size > 0
            if not valid:
                errors.append({'missing_archive_role': {'paper': pid, 'role': role, 'path': key}})
    columns = {}
    links = 0
    compiled = 0
    for p in ROOT.rglob('*'):
        if not p.is_file() or any(part in {'.git', '.venv', 'venv', '__pycache__', 'node_modules'} for part in p.relative_to(ROOT).parts):
            continue
        key = p.relative_to(ROOT).as_posix()
        if p.suffix == '.csv':
            with p.open(encoding='utf-8-sig', newline='') as stream:
                rows = list(csv.reader(stream))
            if not rows or any(len(row) != len(rows[0]) for row in rows):
                errors.append({'invalid_csv_width': key})
                continue
            columns[key] = len(rows[0])
            if key == 'papers/paper_matrix.csv':
                ids = [row[0] for row in rows[1:]]
                if len(ids) != len(set(ids)) or not {'P001', 'P002'} <= set(ids):
                    errors.append({'invalid_paper_ids': ids})
        if p.suffix == '.py':
            try:
                compile(p.read_text(encoding='utf-8-sig'), key, 'exec')
                compiled += 1
            except SyntaxError as exc:
                errors.append({'python_syntax': {'file': key, 'error': str(exc)}})
        if p.suffix != '.md':
            continue
        text = markdown_prose(p.read_text(encoding='utf-8-sig'))
        for url in re.findall(r'!?\[[^\]\n]*\]\(([^\n]*?)\)', text):
            url = re.sub(r'\s+"[^"]*"$', '', url.strip()).strip('<>')
            if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:', url):
                continue
            target = (p.parent / unquote(url.split('#')[0])).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append({'broken_link': {'source': key, 'target': url}})
            else:
                links += 1
        for embed in re.findall(r'!\[\[([^\]]+)\]\]', text):
            target = p.parent / embed.split('|')[0]
            if not target.is_file():
                errors.append({'missing_note_embed': {'source': key, 'target': embed}})
    for key, width in [('papers/paper_matrix.csv', 36),
                       ('docs/innovation_bank/P001_ideas.csv', 10),
                       ('docs/innovation_bank/P002_ideas.csv', 10),
                       ('reproductions/P001_PointPillars_VoD/experiment_tracker.csv', 8),
                       ('reproductions/P002_CRN/experiment_tracker.csv', 8)]:
        if columns.get(key) != width:
            errors.append({'unexpected_schema': {'file': key, 'expected_columns': width}})
    report = {'passed': not errors, 'errors': errors, 'archive_roles': archives,
              'csv_columns': columns, 'existing_markdown_targets': links,
              'python_files_compiled': compiled,
              'claim_boundary': 'Working-tree structure, links, CSV and Python syntax only. No frozen hash, historical ZIP/PDF, teacher acceptance, CUDA, model, training or metric validation.'}
    emit_report(report, args.report)
    return 0 if not errors else 1


if __name__ == '__main__':
    sys.exit(main())
