import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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
    

    # testing text_node_to_html_node
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("Bold me", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold me")
    
    def test_code(self):
        node = TextNode("def hello(): print('Hello')", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "def hello(): print('Hello')")

    def test_link(self):
        node = TextNode("www.brian-cox.com", TextType.LINK, url="www.brian-cox.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "www.brian-cox.com")
        self.assertEqual(html_node.props, {"href":"www.brian-cox.com"})

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )



if __name__ == "__main__":
    unittest.main()