from google import genai
import json
import re

client = genai.Client(api_key="AQ.Ab8RN6JsuEPCwmAGDWmAq69nhQJFeAIYDbX8VMAH_qOx4cZIKw")

def clean_json_block(text: str) -> str:
    text = re.sub(r"^```json", "", text.strip())
    text = re.sub(r"^```", "", text.strip())
    text = re.sub(r"```$", "", text.strip())
    return text.strip()

def generate_quiz(topic: str):
    try:
        prompt = f"""Generate 3 multiple-choice questions about '{topic}'.
Return ONLY valid JSON in this exact format, no extra text:
[
  {{"question": "...", "options": ["A", "B", "C", "D"], "answer": "correct option"}},
  {{"question": "...", "options": ["A", "B", "C", "D"], "answer": "correct option"}},
  {{"question": "...", "options": ["A", "B", "C", "D"], "answer": "correct option"}}
]"""
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )
        cleaned = clean_json_block(response.text)
        quiz = json.loads(cleaned)
        return quiz
    except Exception as e:
        return f"⚠️ Error in Quiz: {e}"