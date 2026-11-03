"""Validate starter JSON catalogs (standard library only)."""
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1] / "database"
for kind in ("characters", "races", "planets", "weapons"):
    path = root / kind / "catalog.json"
    obj = json.loads(path.read_text(encoding="utf-8"))
    assert obj["schema_version"] == 1 and isinstance(obj["entries"], list), path
    print(f"OK {kind}: {len(obj['entries'])} entries")
