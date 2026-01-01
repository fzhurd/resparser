
from dataclasses import dataclass
from typing import List


@dataclass
class ResumeData:
    name: str
    email: str
    skills: List[str]
