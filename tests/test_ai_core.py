
import unittest
from app.ai_agent.ai_core import LootyAI

class TestLootyAI(unittest.TestCase):
    def setUp(self):
        self.looty_ai = LootyAI(api_key="dummy_key", looty_knowledge="LOOTY is an NFT brand." )

    def test_generate_response(self):
        prompt = "What is LOOTY?"
        response = self.looty_ai.generate_response(prompt)
        self.assertIsInstance(response, str, "Response should be a string.")

    def test_analyze_sentiment(self):
        text = "I love LOOTY!"
        sentiment = self.looty_ai.analyze_sentiment(text)
        self.assertIn("label", sentiment[0], "Sentiment analysis should include a label.")
        self.assertIn("score", sentiment[0], "Sentiment analysis should include a score.")

if __name__ == "__main__":
    unittest.main()
