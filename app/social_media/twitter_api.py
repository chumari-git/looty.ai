import tweepy
import os

class TwitterManager:
    def __init__(self, api_key, api_secret, access_token, access_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = access_token
        self.access_secret = access_secret
        self.client = self.authenticate()

    def authenticate(self):
        auth = tweepy.OAuth1UserHandler(
            self.api_key, self.api_secret, self.access_token, self.access_secret
        )
        return tweepy.API(auth)

    def post_tweet(self, content):
        try:
            self.client.update_status(content)
            print("Tweet posted successfully.")
        except Exception as e:
            print(f"Error posting tweet: {e}")
