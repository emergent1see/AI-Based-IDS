from .base_collector import BaseCollector
class NetworkMonitor(BaseCollector):
    def sample(self):
        # placeholder: use psutil.net_io_counters() or pyshark for packet capture
        return {}
