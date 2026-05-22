import unittest

from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestNodeDeliminator(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This has a **bold** bit", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        result = [ TextNode("This has a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" bit", TextType.TEXT),
            ]

        self.assertEqual(result, new_nodes)

        node_2 = TextNode("This has a **bold** bit, followed by **another** one", TextType.TEXT)
        result_2 = [ TextNode("This has a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" bit, followed by ", TextType.TEXT),
            TextNode("another", TextType.BOLD),
            TextNode(" one", TextType.TEXT)
            ]
        
        self.assertEqual(result_2, split_nodes_delimiter([node_2], "**", TextType.BOLD))

        node_list = [node, node_2]

        node_list_result = [ TextNode("This has a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" bit", TextType.TEXT),
            TextNode("This has a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" bit, followed by ", TextType.TEXT),
            TextNode("another", TextType.BOLD),
            TextNode(" one", TextType.TEXT)
            ]

        self.assertEqual(node_list_result, split_nodes_delimiter(node_list, "**", TextType.BOLD))

    def test_italic(self):
        node = TextNode("well we _should_ be italic here", TextType.TEXT)

        result = [ TextNode("well we ", TextType.TEXT),
            TextNode("should", TextType.ITALIC),
            TextNode(" be italic here", TextType.TEXT),
            ]
        
        self.assertEqual(result, split_nodes_delimiter([node], "_", TextType.ITALIC))
                         
    def test_code(self):
        node = TextNode("The variable is 'x = 3*5'", TextType.TEXT)
        
        result = [TextNode("The variable is ", TextType.TEXT),
                  TextNode("x = 3*5", TextType.CODE),
                  TextNode("", TextType.TEXT)
        ]

    def bad_syntax(self):
        node = TextNode("This has a **bold* bit", TextType.TEXT)

        result = [ TextNode("This has a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" bit", TextType.TEXT),
            ]
        
        self.assertNotEqual(result, split_nodes_delimiter([node], "**", TextType.BOLD))

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://wikipedia.org)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://wikipedia.org"),
            ],
            matches,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_link(self):
        node = TextNode(
            "This is text with a [link](brian-cox.com) and another [second link](readersofia.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "brian-cox.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "readersofia.com"
                ),
            ],
            new_nodes,
        )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://wikipedia.org) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://wikipedia.org"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )
if __name__ == "__main__":
    unittest.main()