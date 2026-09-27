from google import genai

client = genai.Client(api_key="AQ.Ab8RN6JsuEPCwmAGDWmAq69nhQJFeAIYDbX8VMAH_qOx4cZIKw")

def summarize_text(text: str) -> str:
    try:
        prompt = f"Summarize the following text in a concise and clear way:\n\n{text}"
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in Summary: {e}"