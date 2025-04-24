import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path, output_txt_path):
    doc = fitz.open(pdf_path)
    all_text = ""

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        all_text += f"\n\n--- Page {page_num + 1} ---\n{text}"

    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write(all_text)

    print(f"✅ Extracted text saved to: {output_txt_path}")
