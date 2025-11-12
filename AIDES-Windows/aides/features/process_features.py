from .base_extractor import BaseExtractor
class ProcessFeatures(BaseExtractor):
    def extract(self, proc_list):
        feats = []
        for p in proc_list:
            feats.append({
                "pid": p.get("pid"),
                "name": p.get("name"),
            })
        return feats
