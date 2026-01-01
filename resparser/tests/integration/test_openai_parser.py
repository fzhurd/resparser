
import os
import pytest

from resparser.com.extractor.skills_extractor import SkillsExtractor
from resparser.com.llm.openai_provider import OpenAILLMProvider
from tests.integration.sample_data import SAMPLE_RESUME_TEXT


pytestmark = pytest.mark.integration


@pytest.mark.skipif(
    not os.getenv("OPENAI_API_KEY"),
    reason="OPENAI_API_KEY not set"
)
def test_openai_skills_extraction_real():
    provider = OpenAILLMProvider(model="gpt-4o-mini")
    extractor = SkillsExtractor(provider)

    skills = extractor.extract(SAMPLE_RESUME_TEXT)

    assert isinstance(skills, list)
    assert len(skills) > 0
    assert any("Python" in s for s in skills)
