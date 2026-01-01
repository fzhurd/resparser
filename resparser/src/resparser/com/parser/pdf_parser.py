import pdfplumber

from ..parser.file_parser import FileParser


# class PDFParser(FileParser):
#     def parse(self, file_path: str) -> str:
#         # Stub: replace with pdfplumber / PyPDF2 in real implementation
#         return """
#         Jane Doe
#         Email: jane.doe@gmail.com
#         Experienced in Python, Machine Learning, and LLM systems.
#         """

class PDFParser(FileParser):
    def parse(self, file_path: str) -> str:
        text_chunks = []

        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text(
                    x_tolerance=2,
                    y_tolerance=2,
                    layout=True
                )
                if page_text:
                    text_chunks.append(page_text)

        return "\n".join(text_chunks)

