
import unittest
from app.content.blog_generator import BlogGenerator

class TestBlogGenerator(unittest.TestCase):
    def setUp(self):
        self.blog_generator = BlogGenerator()

    def test_create_blog(self):
        topic = "NFTs and Digital Art"
        context = "LOOTY is revolutionizing NFTs in the art world."
        blog_content = self.blog_generator.create_blog(topic, context)
        self.assertIsInstance(blog_content, str, "Generated blog content should be a string.")
        self.assertIn("NFTs", blog_content, "Blog content should mention NFTs.")

if __name__ == "__main__":
    unittest.main()
