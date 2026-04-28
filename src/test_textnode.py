import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        node3 = TextNode("This is a text node", TextType.ITALIC)

        # nodes with links
        node4 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        node5 = TextNode("This is some anchor text", TextType.LINK)
        node6 = TextNode("This is some anchor text", TextType.LINK, None)


        node7 = TextNode("This is some anchor text", TextType.IMAGE, "https://www.boot.dev")
        
        # node 1 + 2 equal, should be true
        self.assertEqual(node, node2)

        # node 1 + 3 not equal, should be true
        self.assertNotEqual(node, node3)

        # node 4 + 5 not equal, should be true
        self.assertNotEqual(node4, node5)

        # node 5 + 6 equal, should be true
        self.assertEqual(node, node2)

        # node 6 + 7 not equal, should be true
        self.assertNotEqual(node6, node7)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )




if __name__ == "__main__":
    unittest.main()