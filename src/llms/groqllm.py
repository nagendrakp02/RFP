from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("Groq API Key is required")
        self.groq_api_key = api_key

    def get_llm(self):
        try:
            return ChatGroq(api_key=self.groq_api_key, model="llama-3.3-70b-versatile")
        except Exception as e:
            raise ValueError(f"Error occurred while initializing ChatGroq: {e}")
