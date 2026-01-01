import pytest

from resparser.com.extractor.email_extractor import EmailExtractor
from resparser.com.extractor.name_extractor import NameExtractor
from resparser.com.extractor.resume_extractor_coordinate import ResumeExtractor


def test_missing_skills_key_raises_keyerror():
    extractors = {
        "name": NameExtractor(),
        "email": EmailExtractor(),
        # "skills" intentionally omitted
    }
    with pytest.raises(KeyError):
        ResumeExtractor(extractors).extract("Jane Doe\njane@example.com")


def test_missing_name_key_raises_keyerror():
    extractors = {
        "email": EmailExtractor(),
        # "name" intentionally omitted
        "skills": lambda text: [],  # dummy callable to satisfy typing if accessed
    }
    with pytest.raises(KeyError):
        ResumeExtractor(extractors).extract("Jane Doe\njane@example.com")


def test_missing_email_key_raises_keyerror():
    extractors = {
        "name": NameExtractor(),
        # "email" intentionally omitted
        "skills": lambda text: [],
    }
    with pytest.raises(KeyError):
        ResumeExtractor(extractors).extract("Jane Doe\njane@example.com")
