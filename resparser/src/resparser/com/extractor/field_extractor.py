from abc import ABC, abstractmethod


class FieldExtractor(ABC):
    @abstractmethod
    def extract(self, text: str):
        pass
