# resparser

A minimal, test-driven resume parsing framework for extracting key fields (name, email, skills) from PDF and Word documents. The project demonstrates clean separation of concerns, pluggable parsers, and swappable “skills extraction” strategies using either a mocked LLM, OpenAI, or Google Gemini.

Supported input formats:
- .pdf via pdfplumber
- .docx via python-docx

Python: 3.12+


## Features

- Simple orchestration that chooses a parser based on file extension
- Parsers
  - PDFParser (pdfplumber)
  - WordParser (python-docx)
- Field extractors
  - NameExtractor (naive first non-empty line)
  - EmailExtractor (regex-based)
  - SkillsExtractor (delegates to an LLM-like provider)
- LLM provider implementations
  - Mock (for tests)
  - OpenAI (gpt-4o-mini by default)
  - Gemini (gemini-1.5-flash by default; tests use gemini-flash-latest)
- Thorough unit tests (no network) and optional integration tests (OpenAI/Gemini)
- Minimal public API with a single orchestrator to parse a resume into a dataclass


## Project Structure

```
resparser/
├─ pyproject.toml
├─ src/
│  └─ resparser/
│     └─ com/
│        ├─ data/
│        │  ├─ resume_data.py         # ResumeData dataclass
│        │  ├─ resume.pdf             # Sample PDF
│        │  └─ resume.docx            # Sample Word document
│        ├─ extractor/
│        │  ├─ field_extractor.py     # Base extractor interface
│        │  ├─ name_extractor.py
│        │  ├─ email_extractor.py
│        │  ├─ skills_extractor.py    # Uses an LLM-like provider
│        │  └─ resume_extractor_coordinate.py  # Combines field extractors
│        ├─ llm/
│        │  ├─ llm_provider.py        # Base LLM provider interface
│        │  ├─ openai_provider.py
│        │  └─ gemini_provider.py
│        ├─ orchestration/
│        │  └─ resume_orchestration.py # Selects parser, coordinates extraction
│        └─ parser/
│           ├─ __init__.py
│           ├─ file_parser.py         # Base parser interface
│           ├─ pdf_parser.py
│           └─ word_parser.py
└─ tests/
   ├─ unit/
   │  ├─ fake.py                      # Fake parser returning known text
   │  ├─ mocks.py                     # Mock LLM provider
   │  ├─ test_framework.py
   │  ├─ test_resume_extractor.py
   │  └─ test_skills_extractor.py
   └─ integration/
      ├─ sample_data.py
      ├─ test_pdf_real_data.py
      ├─ test_word_real_data.py
      ├─ test_openai_parser.py        # Requires OPENAI_API_KEY
      └─ test_gemini_parser.py        # Requires GEMINI_API_KEY
```


## Installation

Preferred: PDM (project uses PEP 621 + pdm-backend)

1) Install PDM (one-time)
- Windows: `python -m pip install --user pdm`
- macOS/Linux: `pipx install pdm` (or `python -m pip install --user pdm`)

2) Install dependencies
- From the project root:
  - `pdm install`

Alternative (pip-only quickstart)

If you don’t want PDM, install the runtime deps directly:
- `python -m venv .venv`
- Windows: `.venv\Scripts\activate`
- macOS/Linux: `source .venv/bin/activate`
- `python -m pip install pdfplumber python-docx openai google-generativeai pytest`

Note: Packaging with `pip install -e .` requires `pdm-backend`; using PDM is recommended.


## Quickstart

Programmatic usage (offline skills extraction using the simulated LLM client)

```python
from resparser.com.extractor.name_extractor import NameExtractor
from resparser.com.extractor.email_extractor import EmailExtractor
from resparser.com.extractor.skills_extractor import SkillsExtractor, LLMClient
from resparser.com.extractor.resume_extractor_coordinate import ResumeExtractor
from resparser.com.orchestration.resume_orchestration import ResumeParserFramework

extractors = {
    "name": NameExtractor(),
    "email": EmailExtractor(),
    "skills": SkillsExtractor(LLMClient()),  # uses simple rule-based simulation
}

resume_extractor = ResumeExtractor(extractors)
framework = ResumeParserFramework(resume_extractor)

resume = framework.parse_resume("src/resparser/com/data/resume.pdf")
print(resume)  # ResumeData(name=..., email=..., skills=[...])
```

Using OpenAI for skills extraction

```python
import os
from resparser.com.extractor.name_extractor import NameExtractor
from resparser.com.extractor.email_extractor import EmailExtractor
from resparser.com.extractor.skills_extractor import SkillsExtractor
from resparser.com.extractor.resume_extractor_coordinate import ResumeExtractor
from resparser.com.orchestration.resume_orchestration import ResumeParserFramework
from resparser.com.llm.openai_provider import OpenAILLMProvider

os.environ["OPENAI_API_KEY"] = "<your key>"

extractors = {
    "name": NameExtractor(),
    "email": EmailExtractor(),
    "skills": SkillsExtractor(OpenAILLMProvider(model="gpt-4o-mini")),
}

framework = ResumeParserFramework(ResumeExtractor(extractors))
resume = framework.parse_resume("src/resparser/com/data/resume.pdf")
print(resume.skills)
```

Using Gemini for skills extraction

```python
import os
from resparser.com.extractor.name_extractor import NameExtractor
from resparser.com.extractor.email_extractor import EmailExtractor
from resparser.com.extractor.skills_extractor import SkillsExtractor
from resparser.com.extractor.resume_extractor_coordinate import ResumeExtractor
from resparser.com.orchestration.resume_orchestration import ResumeParserFramework
from resparser.com.llm.gemini_provider import GeminiLLMProvider

os.environ["GEMINI_API_KEY"] = "<your key>"

extractors = {
    "name": NameExtractor(),
    "email": EmailExtractor(),
    "skills": SkillsExtractor(GeminiLLMProvider(model="gemini-1.5-flash")),
}

framework = ResumeParserFramework(ResumeExtractor(extractors))
resume = framework.parse_resume("src/resparser/com/data/resume.docx")
print(resume.skills)
```

Notes
- Orchestrator supports only `.pdf` and `.docx`. Other extensions will raise ValueError.
- When running scripts directly from the repo, prefer `pdm run python your_script.py` so `src/` is on sys.path. Otherwise, set `PYTHONPATH=src` manually.


## Configuration

Environment variables for integration tests / real LLM providers:
- OPENAI_API_KEY
- GEMINI_API_KEY

Set them for the current shell session:
- PowerShell:
  - `$env:OPENAI_API_KEY="..."` and/or `$env:GEMINI_API_KEY="..."`
- cmd.exe:
  - `set OPENAI_API_KEY=...` and/or `set GEMINI_API_KEY=...`
- bash/zsh:
  - `export OPENAI_API_KEY=...` and/or `export GEMINI_API_KEY=...`

For persistent storage on Windows, `setx` can be used (requires new shell).


## Running Tests

All tests (quick, excluding real LLM integrations)
- With PDM: `pdm run pytest -q -m "not integration"`
- With venv: `pytest -q -m "not integration"`

Only unit tests (no network, fastest)
- With PDM: `pdm run pytest -q tests/unit`
- With venv: `pytest -q tests/unit`

Run integration tests against real LLMs
- OpenAI:
  - Ensure `OPENAI_API_KEY` is set
  - `pytest -q -m integration tests/integration/test_openai_parser.py`
- Gemini:
  - Ensure `GEMINI_API_KEY` is set
  - `pytest -q -m integration tests/integration/test_gemini_parser.py`

Parse real sample files (no network)
- PDF sample: `tests/integration/test_pdf_real_data.py`
- Word sample: `tests/integration/test_word_real_data.py`


## Unit Test Coverage

- tests/unit/test_email_extractor.py — basic, none, multiple, uppercase emails
- tests/unit/test_name_extractor.py — trims, skips numeric/punct-only, empty input
- tests/unit/test_skills_extractor_more.py — built-in LLMClient: multiple/no skills
- tests/unit/test_resume_orchestration_parser_selection.py — parser selection and unsupported; uses pytest.importorskip for pdfplumber/docx
- tests/unit/test_resume_extractor_edge_cases.py — KeyError when extractor keys missing

Testing notes:
- tests/conftest.py adds src to sys.path so imports of resparser work without installing the package.
- Orchestrator lazily imports PDF/Word parsers to avoid import-time failures when optional deps are missing.
- Unit tests require no API keys and no network.

## Design Overview

- Strategy pattern for file parsing
  - `FileParser` is the interface; `PDFParser` and `WordParser` are implementations.
- Field extraction pipeline
  - `NameExtractor`, `EmailExtractor`, `SkillsExtractor` each handle one field.
  - `ResumeExtractor` composes them and returns a single `ResumeData` dataclass.
- Pluggable skill extraction
  - `SkillsExtractor` delegates to an LLM-like provider with `extract_skills(text) -> list[str]`.
  - Drop-in providers: `OpenAILLMProvider`, `GeminiLLMProvider`, or a mock/stub for tests.


## Limitations and Notes

- Name extraction is intentionally naive (first non-empty line).
- Email extraction uses a simple regex and may capture non-primary emails if multiple exist.
- Skills extraction results depend on the provider’s quality. The OpenAI/Gemini providers expect a JSON array response and include basic safety parsing.
- PDF text extraction quality varies with document layout and encoding. `pdfplumber` options (`x_tolerance`, `y_tolerance`, `layout=True`) are set conservatively; adjust as needed.
- Word extraction includes paragraph and table text; complex layouts may require additional handling.
- Only `.pdf` and `.docx` are supported.


## License

MIT (see `pyproject.toml` for license metadata)
