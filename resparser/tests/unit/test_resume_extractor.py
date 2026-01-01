
from resparser.com.extractor.email_extractor import EmailExtractor
from resparser.com.extractor.name_extractor import NameExtractor
from resparser.com.extractor.resume_extractor_coordinate import ResumeExtractor
from resparser.com.extractor.skills_extractor import SkillsExtractor
from tests.unit.mocks import MockLLMProvider


def test_resume_extractor_combines_fields():
    extractors = {
        "name": NameExtractor(),
        "email": EmailExtractor(),
        "skills": SkillsExtractor(MockLLMProvider()),
    }

    extractor = ResumeExtractor(extractors)

    text = """
    Jane Doe
    jane.doe@gmail.com
    Python ML
    """

    resume = extractor.extract(text)

    assert resume.name == "Jane Doe"
    assert resume.email == "jane.doe@gmail.com"
    assert resume.skills == ["Python", "Machine Learning"]
