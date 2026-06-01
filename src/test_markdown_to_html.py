import unittest
from markdown_to_html import markdown_to_html_node


class TestTextNode(unittest.TestCase):
    def test_simple(self):
        md = "A plain sentence here"
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><p>A plain sentence here</p></div>")

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_unordered_list(self):
        md = """
- This is a list item with **bold**
- Another item with _italic_
- A third plain item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list item with <b>bold</b></li><li>Another item with <i>italic</i></li><li>A third plain item</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. First item with `code`
2. Second item
3. Third item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item with <code>code</code></li><li>Second item</li><li>Third item</li></ol></div>",
        )


if __name__ == "__main__":
    unittest.main()