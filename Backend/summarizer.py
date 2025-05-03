
import os
from google import genai
from google.genai import types

def load_text_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def build_prompt(paper_text):
    return f"""
You are an academic assistant.

The following text is extracted from a research paper. It may include formatting artifacts, citations, references, or other irrelevant sections.

Your task is to:
- Ignore irrelevant metadata, footnotes, references, and formatting noise
- Provide a detailed, human-readable summary of the core content: introduction, problem statement, methodology, results, discussion, and conclusion if available
- Keep the summary accurate, objective, and comprehensive

Here is the text:
\"\"\"{paper_text}\"\"\"
"""

def generate_summary(input_txt_path):
    # Load and prepare the prompt
    paper_text = load_text_from_file(input_txt_path)
    full_prompt = build_prompt(paper_text)

    # Set up Gemini client
    client = genai.Client(api_key="key")
    model = "gemini-2.5-flash-preview-04-17"

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=full_prompt),
            ],
        ),
    ]

    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    print("\n🔍 Generating summary...\n")
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        with open("summary.txt", "a", encoding="utf-8") as out:
          out.write(chunk.text)
 

if __name__ == "__main__":
    input_file = "extracted_text.txt" 
    generate_summary(input_file)
