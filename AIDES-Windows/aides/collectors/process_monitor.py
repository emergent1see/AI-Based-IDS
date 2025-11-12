import psutil
from .base_collector import BaseCollector
class ProcessMonitor(BaseCollector):
    def __init__(self, config=None):
        super().__init__(config)
    def start(self): pass
    def stop(self): pass
    def sample(self):
        procs = []
        for p in psutil.process_iter(['pid','name','exe','create_time']):
            procs.append(p.info)
        return procs
