"""Compatibility entry for the current P001-only resource validation."""
from pathlib import Path
import runpy,sys
root=Path(__file__).resolve().parents[1]
sys.argv=[str(root/'scripts/validate_lab.py'),*sys.argv[1:]]
sys.path.insert(0,str(root/'scripts'))
runpy.run_path(sys.argv[0],run_name='__main__')
