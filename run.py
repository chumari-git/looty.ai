from app.ai_agent.ai_core import LootyAI
from app.social_media.twitter_api import TwitterManager
from app.content.blog_generator import BlogGenerator
from app.crypto.tokenomics import LootyToken
import config.settings as settings


def main():
    # Initialize LOOTY AI
    looty_ai = LootyAI(
        api_key=settings.OPENAI_API_KEY,
        looty_knowledge=settings.LOOTY_KNOWLEDGE_BASE,
    )
    
    # Initialize Twitter Manager
    twitter_manager = TwitterManager(
        api_key=settings.TWITTER_API_KEY,
        api_secret=settings.TWITTER_API_SECRET,
        access_token=settings.TWITTER_ACCESS_TOKEN,
        access_secret=settings.TWITTER_ACCESS_SECRET,
    )
    
    # Initialize Blog Generator
    blog_generator = BlogGenerator()
    
    # Initialize Cryptocurrency Token
    looty_token = LootyToken(rpc_url=settings.BLOCKCHAIN_RPC_URL)
    
    # Example Task 1: Post a tweet
    tweet_content = "Discover the latest in NFTs and crypto with LOOTY! Visit us at https://www.looty.art #NFTs #Crypto"
    twitter_manager.post_tweet(tweet_content)
    
    # Example Task 2: Generate a blog
    blog_topic = "The Future of NFTs in Digital Art"
    blog_content = blog_generator.create_blog(topic=blog_topic, looty_context=settings.LOOTY_CONTEXT)
    print(f"Generated Blog Content:\n{blog_content}")
    
    # Example Task 3: Deploy a LOOTY Token
    token_name = "LOOTYToken"
    token_symbol = "LTY"
    token_supply = 1000000
    print(f"Creating LOOTY Token: {token_name} ({token_symbol}) with a supply of {token_supply}")
    # Uncomment to deploy token (requires blockchain connection)
    # looty_token.create_token(name=token_name, symbol=token_symbol, total_supply=token_supply)
    

if __name__ == "__main__":
    main()
