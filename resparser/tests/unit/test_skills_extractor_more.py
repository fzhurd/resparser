from resparser.com.extractor.skills_extractor import SkillsExtractor, LLMClient


def test_builtin_llmclient_detects_multiple_skills():
    text = "Experienced in Python and LLM with Data Engineering background"
    extractor = SkillsExtractor(LLMClient())
    assert extractor.extract(text) == ["Python", "LLM", "Data Engineering"]


def test_builtin_llmclient_returns_empty_when_no_skills():
    text = "Experienced software developer with strong problem solving"
    extractor = SkillsExtractor(LLMClient())
    assert extractor.extract(text) == []
