import pytest
from resparser.com.orchestration.resume_orchestration import ResumeParserFramework
from resparser.com.extractor.resume_extractor_coordinate import ResumeExtractor

pytest.importorskip("pdfplumber")
pytest.importorskip("docx")

from resparser.com.parser.pdf_parser import PDFParser
from resparser.com.parser.word_parser import WordParser


def test_get_parser_selects_pdf():
    framework = ResumeParserFramework(ResumeExtractor({}))
    parser = framework._get_parser("resume.pdf")
    assert isinstance(parser, PDFParser)


def test_get_parser_selects_docx():
    framework = ResumeParserFramework(ResumeExtractor({}))
    parser = framework._get_parser("resume.docx")
    assert isinstance(parser, WordParser)


def test_get_parser_unsupported_raises():
    framework = ResumeParserFramework(ResumeExtractor({}))
    try:
        framework._get_parser("resume.txt")
        assert False, "Expected ValueError for unsupported file format"
    except ValueError as e:
        assert "Unsupported file format" in str(e)
