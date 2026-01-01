from ..extractor.field_extractor import FieldExtractor


class NameExtractor(FieldExtractor):
    def extract(self, text: str) -> str:
        # Very naive: first non-empty line
        for line in text.splitlines():
            line = line.strip()
            if line and any(c.isalpha() for c in line):
                return line
        return ""
