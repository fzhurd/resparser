# tests/integration/test_gemini_integration.py
import os
import pytest

from resparser.com.extractor.skills_extractor import SkillsExtractor
from resparser.com.llm.gemini_provider import GeminiLLMProvider
from tests.integration.sample_data import SAMPLE_RESUME_TEXT

pytestmark = pytest.mark.integration

@pytest.mark.skipif(
    not os.getenv("GEMINI_API_KEY"),
    reason="GEMINI_API_KEY not set"
)
def test_gemini_skills_extraction_real():
    provider = GeminiLLMProvider(model="gemini-flash-latest")
    extractor = SkillsExtractor(provider)

    skills = extractor.extract(SAMPLE_RESUME_TEXT)

    assert isinstance(skills, list)
    assert len(skills) > 0
    assert any("Machine" in s for s in skills)
