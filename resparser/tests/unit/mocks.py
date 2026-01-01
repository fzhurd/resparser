from typing import List

from resparser.com.llm.llm_provider import LLMProvider


class MockLLMProvider(LLMProvider):
    def extract_skills(self, resume_text: str) -> List[str]:
        return ["Python", "Machine Learning"]