# platform_adapter.py
from abc import ABC, abstractmethod

class PlatformAdapter(ABC):
    @abstractmethod
    def translate_pipeline(self, pipeline):
        pass

    @abstractmethod
    def execute_pipeline(self, pipeline):
        pass
