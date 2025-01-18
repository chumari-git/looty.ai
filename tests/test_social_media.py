
import unittest
from unittest.mock import MagicMock
from app.social_media.twitter_api import TwitterManager

class TestTwitterManager(unittest.TestCase):
    def setUp(self):
        self.twitter_manager = TwitterManager("api_key", "api_secret", "access_token", "access_secret")
        self.twitter_manager.client = MagicMock()

    def test_post_tweet(self):
        content = "Test tweet content."
        self.twitter_manager.post_tweet(content)
        self.twitter_manager.client.update_status.assert_called_once_with(content)

if __name__ == "__main__":
    unittest.main()
