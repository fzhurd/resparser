
import os
from typing import List

from openai import OpenAI

from ..llm.llm_provider import LLMProvider


class OpenAILLMProvider(LLMProvider):
    def __init__(self, model: str = "gpt-4o-mini"):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model

    def extract_skills(self, resume_text: str) -> List[str]:
        prompt = f"""
        Extract a list of professional skills from the resume text below.
        Return ONLY a JSON array of strings.

        Resume:
        {resume_text}
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert resume parser."},
                {"role": "user", "content": prompt},
            ],
            temperature=0,
        )

        content = response.choices[0].message.content
        return self._safe_parse_json_array(content)

    def _safe_parse_json_array(self, content: str) -> List[str]:
        import json
        try:
            return json.loads(content)
        except Exception:
            return []
