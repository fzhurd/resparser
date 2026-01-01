import os
from typing import List

import google.generativeai as genai

from ..llm.llm_provider import LLMProvider


class GeminiLLMProvider(LLMProvider):
    def __init__(self, model: str = "gemini-1.5-flash"):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel(model)

    def extract_skills(self, resume_text: str) -> List[str]:
        prompt = f"""
        Extract professional skills from the resume below.
        Output ONLY a JSON array of strings.

        Resume:
        {resume_text}
        """

        response = self.model.generate_content(prompt)
        return self._safe_parse_json_array(response.text)

    def _safe_parse_json_array(self, content: str) -> List[str]:
        import json
        try:
            return json.loads(content)
        except Exception:
            return []
