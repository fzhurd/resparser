import re

from ..extractor.field_extractor import FieldExtractor


class EmailExtractor(FieldExtractor):
    EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    def extract(self, text: str) -> str:
        match = re.search(self.EMAIL_REGEX, text)
        return match.group(0) if match else ""
