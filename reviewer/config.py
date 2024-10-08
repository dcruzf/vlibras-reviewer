import json
from pathlib import Path


p  = Path(__file__).parents[1] / "config.json"
config = json.loads(p.read_bytes())