from transformers import pipeline
import openai

class LootyAI:
    def __init__(self, api_key, looty_knowledge):
        openai.api_key = api_key
        self.knowledge_base = looty_knowledge
        self.sentiment_analysis = pipeline("sentiment-analysis")

    def generate_response(self, prompt):
        """Generate AI response aligned with LOOTY's brand voice."""
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"Embody the LOOTY brand: {self.knowledge_base}."},
                {"role": "user", "content": prompt},
            ],
        )
        return response["choices"][0]["message"]["content"]

    def analyze_sentiment(self, text):
        """Analyze sentiment of a given text."""
        return self.sentiment_analysis(text)
