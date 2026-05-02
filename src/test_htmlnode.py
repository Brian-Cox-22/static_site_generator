import unittest

from htmlnode import HTMLNode, LeafNode

class HtmlTest(unittest.TestCase):


    # now with some stuff
    correct_node = {"Tag":"p",
                    "Value":"Test Paragraph",
                    "Children":None,
                    "Props":{
                            "href": "https://www.google.com",
                            "target": "_blank",}
                            }
        
    test_node = HTMLNode("p", "Test Paragraph", props={
                            "href": "https://www.google.com",
                            "target": "_blank",})
    
    def test_constructor(self):
        node = HTMLNode()
        node2 = HTMLNode()

        # empty
        self.assertEqual(node.props, node2.props)
        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.children, node2.children)
        self.assertEqual(node.value, node2.value)

        # tag
        self.assertEqual(self.correct_node["Tag"], self.test_node.tag)

        # props
        self.assertEqual(self.correct_node["Props"], self.test_node.props)

    def test_repr(self):
        node = self.test_node
        self.assertEqual(
           "Tag = p,\n value = Test Paragraph,\n children = None,\n props = {'href': 'https://www.google.com', 'target': '_blank'}",
             repr(node)
        )
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    