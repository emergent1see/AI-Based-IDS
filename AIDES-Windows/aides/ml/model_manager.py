import joblib
from pathlib import Path
class ModelManager:
    def __init__(self, model_dir):
        self.model_dir = Path(model_dir)
        self.model_dir.mkdir(parents=True, exist_ok=True)
    def load(self, name):
        p = self.model_dir / f"{name}.pkl"
        if p.exists():
            return joblib.load(p)
        return None
    def save(self, name, model):
        joblib.dump(model, self.model_dir / f"{name}.pkl")
