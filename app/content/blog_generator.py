from transformers import pipeline

class BlogGenerator:
    def __init__(self):
        self.generator = pipeline("text-generation", model="gpt-3.5-turbo")

    def create_blog(self, topic, looty_context):
        """Generate an SEO-optimized blog post."""
        prompt = f"Write a detailed blog about {topic} in the context of LOOTY: {looty_context}"
        response = self.generator(prompt, max_length=1000)
        return response[0]["generated_text"]
