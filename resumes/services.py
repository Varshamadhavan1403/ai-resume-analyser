from pathlib import Path

from pypdf import PdfReader
from docx import Document


class ResumeParser:

    @staticmethod
    def parse(file_path):
        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return ResumeParser.parse_pdf(file_path)

        elif extension == ".docx":
            return ResumeParser.parse_docx(file_path)

        return ""

    @staticmethod
    def parse_pdf(file_path):
        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    @staticmethod
    def parse_docx(file_path):
        doc = Document(file_path)

        text = "\n".join(
            paragraph.text
            for paragraph in doc.paragraphs
        )

        return text