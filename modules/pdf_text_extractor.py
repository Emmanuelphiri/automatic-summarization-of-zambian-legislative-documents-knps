import requests
from io import BytesIO
from pdfminer.high_level import extract_text

def extract_text_from_pdf_url(pdf_url):
    # Download PDF from the URL
    response = requests.get(pdf_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract text using pdfminer.six
        pdf_bytes = BytesIO(response.content)
        extracted_text = extract_text(pdf_bytes)

        return extracted_text
    else:
        print(f"Failed to download PDF from {pdf_url}. Status code: {response.status_code}")
        return None
