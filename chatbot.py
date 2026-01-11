from google import genai
from google.genai import errors

class Chatbot:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API Key is required.")
        
        self.client = genai.Client(api_key=api_key)
        self.model_id = "gemini-2.5-flash" # Use a valid model ID for 2026

    def reply(self, msg: str) -> str:
        prompt = msg.strip()
        if not prompt:
            return "Empty message."

        try:
            # New syntax: client.models.generate_content
            response = self.client.models.generate_content(
                model=self.model_id, 
                contents=prompt
            )
            return response.text or "No response from model."

        except errors.ClientError as e:
            if e.code == 429:
                return "Rate limit hit. Wait 60 seconds."
            return f"API Error: {e.message}"
        except Exception as e:
            return f"Unexpected Error: {str(e)}"