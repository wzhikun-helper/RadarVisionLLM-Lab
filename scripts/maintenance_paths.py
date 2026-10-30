"""P001 resource paths and explicit historical text access; never regenerate PPTs."""
from pathlib import Path
import json,zipfile,hashlib
ROOT=Path(__file__).resolve().parents[1]

def resolve_recorded_file(path):
    p=Path(path)
    if not p.is_absolute():p=ROOT/p
    if p.is_file():return p
    if p.resolve()==(ROOT/'paper_notes/P001_MultiClass_Road_User_Detection.md').resolve():
        return ROOT/'paper_notes/P001_论文精读.md'
    raise FileNotFoundError('Resource retired or missing: '+str(p))

def emit_report(report,destination=None):
    text=json.dumps(report,ensure_ascii=False,indent=2)
    if destination:
        with Path(destination).open('x',encoding='utf-8') as f:f.write(text+'\n')
    print(text)
