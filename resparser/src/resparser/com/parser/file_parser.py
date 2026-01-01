from abc import ABC, abstractmethod


class FileParser(ABC):
    @abstractmethod
    def parse(self, file_path: str) -> str:
        """Return raw text extracted from the file."""
        pass
