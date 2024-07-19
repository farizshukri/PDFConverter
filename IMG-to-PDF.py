from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import sys

def convert_image_to_pdf(image_path, pdf_path):
    try:
        # Open the image file
        image = Image.open(image_path)
        
        # Create a new PDF document
        c = canvas.Canvas(pdf_path, pagesize=image.size)
        
        # Draw the image on the PDF
        c.drawImage(image_path, 0, 0, *image.size)
        
        # Save the PDF document
        c.save()
        
        print(f"PDF saved successfully at: {pdf_path}")
    
    except Exception as e:
        print(f"Error converting image to PDF: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python image_to_pdf.py <image_path> <pdf_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    pdf_path = sys.argv[2]
    
    convert_image_to_pdf(image_path, pdf_path)
