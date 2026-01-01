from ..data.resume_data import ResumeData
from ..extractor.field_extractor import FieldExtractor


class ResumeExtractor:
    def __init__(self, field_extractors: dict[str, FieldExtractor]):
        self.field_extractors = field_extractors

    def extract(self, text: str) -> ResumeData:
        return ResumeData(
            name=self.field_extractors["name"].extract(text),
            email=self.field_extractors["email"].extract(text),
            skills=self.field_extractors["skills"].extract(text),
        )
