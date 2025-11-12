from abc import ABC, abstractmethod
class BaseCollector(ABC):
    def __init__(self, config=None):
        self.config = config
    @abstractmethod
    def start(self): ...
    @abstractmethod
    def stop(self): ...
    @abstractmethod
    def sample(self): ...
