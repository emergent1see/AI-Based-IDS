from .base_collector import BaseCollector
class ETWCollector(BaseCollector):
    def sample(self):
        # ETW on windows: integrate with ETW provider libraries
        return {}
