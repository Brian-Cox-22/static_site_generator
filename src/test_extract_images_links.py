import unittest

from extract_images_links import extract_markdown_images, extract_markdown_link

class TestTextNode(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "   This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_link(
            " Here is text with a [link](https.brian-cox.com)"
        )
        self.assertListEqual([("link", "https.brian-cox.com")], matches)