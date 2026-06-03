import unittest
from markdown_to_html import markdown_to_html_node, extract_title


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

    def test_heading(self):
        md = """
# This is **bolded** header
"""

        node = markdown_to_html_node(md)
        # print(node)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is <b>bolded</b> header</h1></div>",
        )

    def test__2_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )


    def test_block_quote(self):
        md = """
> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><blockquote>"I am in fact a Hobbit in all but size."  -- J.R.R. Tolkien</blockquote></div>',
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

    def test_extract_title(self):
        md = """
# Header
## Subheader
Shawowsa
Wigglywiggly
"""
        title = extract_title(md)
        self.assertEqual(title, "Header")


    def test_extract_title_2_headers(self):
        md = """
# Header
## Subheader
Shawowsa
# Fakeout header
Wigglywiggly
"""
        title = extract_title(md)
        self.assertEqual(title, "Header")
    






if __name__ == "__main__":
    unittest.main()