
from typing import List

from resparser.com.extractor.skills_extractor import SkillsExtractor
from resparser.com.llm.llm_provider import LLMProvider
from tests.unit.mocks import MockLLMProvider


def test_skills_extractor_uses_llm():
    llm = MockLLMProvider()
    extractor = SkillsExtractor(llm)

    text = "Experienced Python developer"
    skills = extractor.extract(text)

    assert skills == ["Python", "Machine Learning"]
