import PyPDF2
import docx

def extract_text(file):
    if not file:
        return ""

    ext = file.name.split(".")[-1].lower()

    if ext == "pdf":
        reader = PyPDF2.PdfReader(file)
        return " ".join(page.extract_text() or "" for page in reader.pages)

    if ext == "docx":
        doc = docx.Document(file)
        return " ".join(p.text for p in doc.paragraphs)

    if ext == "txt":
        return file.read().decode("utf-8")

    return ""
