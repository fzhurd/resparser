from ..data.resume_data import ResumeData
from ..extractor.resume_extractor_coordinate import ResumeExtractor
from ..parser.file_parser import FileParser
from ..parser.pdf_parser import PDFParser
from ..parser.word_parser import WordParser


class ResumeParserFramework:
    def __init__(self, resume_extractor: ResumeExtractor):
        self.resume_extractor = resume_extractor

    def parse_resume(self, file_path: str) -> ResumeData:
        parser = self._get_parser(file_path)
        raw_text = parser.parse(file_path)
        return self.resume_extractor.extract(raw_text)

    def _get_parser(self, file_path: str) -> FileParser:
        if file_path.endswith(".pdf"):
            return PDFParser()
        elif file_path.endswith(".docx"):
            return WordParser()
        else:
            raise ValueError("Unsupported file format")
