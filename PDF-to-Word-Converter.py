import fitz  # PyMuPDF
from docx import Document
from docx.shared import Inches

def pdf_to_docx(pdf_file, docx_file):
    doc = Document()
    pdf_document = fitz.open(pdf_file)
    
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text("text")
        
        # Add page break except for the first page
        if page_num > 0:
            doc.add_page_break()
        
        doc.add_paragraph(text)
    
    doc.save(docx_file)
    print(f"PDF converted to DOCX: {docx_file}")

if __name__ == "__main__":
    pdf_file = input("Enter the input PDF filename: ").strip()
    docx_file = input("Enter the output DOCX filename: ").strip()
    
    pdf_to_docx(pdf_file, docx_file)
