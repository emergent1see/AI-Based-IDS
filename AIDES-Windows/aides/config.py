import yaml
from pathlib import Path
config_path = Path(__file__).parent.parent / "config" / "config.yaml"
def load_config(path=None):
    p = Path(path) if path else config_path
    with open(p, "r") as fh:
        return yaml.safe_load(fh)
