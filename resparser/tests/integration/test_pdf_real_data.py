
from pathlib import Path

from resparser.com.extractor.email_extractor import EmailExtractor
from resparser.com.extractor.name_extractor import NameExtractor
from resparser.com.extractor.resume_extractor_coordinate import ResumeExtractor
from resparser.com.extractor.skills_extractor import SkillsExtractor
from resparser.com.orchestration.resume_orchestration import ResumeParserFramework
from tests.unit.mocks import MockLLMProvider


def test_parse_real_pdf_file():
    extractors = {
        "name": NameExtractor(),
        "email": EmailExtractor(),
        "skills": SkillsExtractor(MockLLMProvider()),
    }

    resume_extractor = ResumeExtractor(extractors)
    framework = ResumeParserFramework(resume_extractor)

    # Resolve real PDF path
    pdf_path = Path(__file__).parent.parent.parent /"src"/"resparser" / "com"/ "data"/ "resume.pdf"

    assert pdf_path.exists(), "resume.pdf not found in data/ directory"

    resume = framework.parse_resume(str(pdf_path))

    assert resume.name == "FIRST   LAST"
    assert resume.email == "sampleresume@gmail.com"
    assert resume.skills == ["Python", "Machine Learning"]

