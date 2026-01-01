
from resparser.com.extractor.email_extractor import EmailExtractor
from resparser.com.extractor.name_extractor import NameExtractor
from resparser.com.extractor.resume_extractor_coordinate import ResumeExtractor
from resparser.com.extractor.skills_extractor import SkillsExtractor
from resparser.com.orchestration.resume_orchestration import ResumeParserFramework
from tests.unit.fake import FakeParser
from tests.unit.mocks import MockLLMProvider


class TestFramework(ResumeParserFramework):
    def _get_parser(self, file_path: str):
        return FakeParser()


def test_framework_end_to_end():
    extractors = {
        "name": NameExtractor(),
        "email": EmailExtractor(),
        "skills": SkillsExtractor(MockLLMProvider()),
    }

    resume_extractor = ResumeExtractor(extractors)
    framework = TestFramework(resume_extractor)

    resume = framework.parse_resume("dummy.pdf")

    assert resume.name == "Jane Doe"
    assert resume.email == "jane.doe@gmail.com"
    assert resume.skills == ["Python", "Machine Learning"]

