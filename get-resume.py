import requests
import json
from pdf2image import convert_from_path

JSON_FILE_NAME = "resume.json"
PDF_FILE_NAME = "Sydney Lin - Resume.pdf"
PNG_FILE_NAME = "resume.png"

# Step 1: Generate the PDF and save it locally
def generate_resume_pdf():
    url = "https://resumake.io/api/generate/resume"
    
    # Load resume data from JSON file
    with open(JSON_FILE_NAME, "r") as file:
        data = json.load(file)

    response = requests.post(url, json=data)

    if response.status_code == 200:
        with open(PDF_FILE_NAME, "wb") as file:
            file.write(response.content)
        print("PDF resume generated successfully.")
    else:
        print("Failed to generate resume.")

# Step 2: Convert only the first page of the PDF to PNG
def convert_first_page_to_png(pdf_path, png_path):
    # Convert the first page of the PDF to an image
    images = convert_from_path(pdf_path, first_page=1, last_page=1)
    
    # Save the first page as a PNG file
    images[0].save(png_path, "PNG")
    print(f"Saved {png_path}")

# Run the functions
generate_resume_pdf()  # Step 1: Generate the PDF
convert_first_page_to_png(PDF_FILE_NAME, PNG_FILE_NAME)  # Step 2: Convert first page to PNG
