# usegemini.py
import asyncio
import os
import google.generativeai as genai
from dotenv import load_dotenv


class ModelGemini:
    def __init__(self):
        load_dotenv()
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not self.gemini_api_key:
            raise ValueError("GEMINI_API_KEY is not set in the .env file.")
        
        genai.configure(api_key=self.gemini_api_key)
        
        # Reuse the same model instance (faster + avoids rate limits)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    async def gemini_response(self, prompt: str) -> str:
        """
        Properly async wrapper for Gemini API using generate_content_async
        """
        try:
            # This is the correct async method!
            response = await self.model.generate_content_async(prompt)
            return response.text
        except Exception as e:
            return f"[Gemini API Error: {str(e)}]"