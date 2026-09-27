import os
from google import genai

client = genai.Client(api_key="AQ.Ab8RN6JsuEPCwmAGDWmAq69nhQJFeAIYDbX8VMAH_qOx4cZIKw")

def answer_question_with_gemini(question: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=question
        )
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in QnA: {e}"