from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_pdf(title, agenda, path='output'):
    if not os.path.exists(path):
        os.makedirs(path)

    file_path = os.path.join(path, f"{title}.pdf")
    c = canvas.Canvas(file_path, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(50, 750, f"Meeting Title: {title}")
    y = 720
    for line in agenda.split('\n'):
        c.drawString(50, y, line)
        y -= 15
        if y < 40:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = 750
    c.save()
    return file_path
