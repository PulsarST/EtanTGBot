import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)
model = "gemini-2.5-flash"

process_raw_text_promt = ""
json_from_text_prompt = ""

with open("./assets/processing_sutdent_input.txt", encoding="utf-8") as file1:
    process_raw_text_promt = file1.read()

with open("./assets/json_from_text_promt.txt", encoding="utf-8") as file2:
    json_from_text_prompt = file2.read()
