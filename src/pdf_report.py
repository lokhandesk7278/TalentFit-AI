from fpdf import FPDF

def safe_text(text):
    return text.encode("latin-1", "replace").decode("latin-1")

def generate_pdf(score, matched, missing):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, safe_text("Resume Job Fit Report"), ln=True)
    pdf.cell(200, 10, safe_text(f"Match Score: {round(score,2)}%"), ln=True)

    pdf.ln(5)
    pdf.cell(200, 10, safe_text("Matched Skills:"), ln=True)
    for s in matched:
        pdf.cell(200, 8, safe_text(f"- {s}"), ln=True)

    pdf.ln(5)
    pdf.cell(200, 10, safe_text("Missing Skills:"), ln=True)
    for s in missing:
        pdf.cell(200, 8, safe_text(f"- {s}"), ln=True)

    path = "resume_report.pdf"
    pdf.output(path)
    return path
