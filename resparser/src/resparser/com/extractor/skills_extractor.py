from ..extractor.field_extractor import FieldExtractor


class LLMClient:
    """
    Simulated LLM client.
    Replace with real API calls (Gemini/OpenAI/etc).
    """
    def extract_skills(self, text: str) -> list[str]:
        # Fake "ML inference"
        known_skills = [
            "Python",
            "Machine Learning",
            "ML",
            "LLM",
            "Data Engineering"
        ]
        return [skill for skill in known_skills if skill in text]


class SkillsExtractor(FieldExtractor):
    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client

    def extract(self, text: str) -> list[str]:
        return self.llm_client.extract_skills(text)
