from google import genai

client = genai.Client(api_key="AQ.Ab8RN6JsuEPCwmAGDWmAq69nhQJFeAIYDbX8VMAH_qOx4cZIKw")

def get_learning_recommendations(topic: str) -> str:
    try:
        prompt = f"""Create a structured learning path for someone who wants to learn '{topic}'.
Include: beginner to advanced stages, a rough timeline, and suggested topics to study at each stage.
Keep it clear and easy to follow."""
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in Learning Path: {e}"