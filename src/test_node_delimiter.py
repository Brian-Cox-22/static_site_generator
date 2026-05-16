import unittest

from node_delimiter import split_nodes_delimiter
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

if __name__ == "__main__":
    unittest.main()