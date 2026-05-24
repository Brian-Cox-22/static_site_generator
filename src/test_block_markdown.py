import unittest


from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class TestNodeDeliminator(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_markdown_to_blocks_newlines(self):
                md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
                blocks = markdown_to_blocks(md)
                self.assertEqual(
                    blocks,
                    [
                        "This is **bolded** paragraph",
                        "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                        "- This is a list\n- with items",
                    ],
                )
    
    # Testing Block to block types

    # headings
        def test_block_to_block_heading(self):
            md_blocks = "# My heading"
            block = block_to_block_type(md_blocks)

            self.assertEqual(block, BlockType.HEADING)

        def test_block_to_block_heading_2(self):
            md_blocks = "# My heading \n #And Another"
            block = block_to_block_type(md_blocks)

            self.assertEqual(block, BlockType.HEADING)
        
        def test_block_to_block_heading_3(self):
            md_blocks = "####### My heading"
            block = block_to_block_type(md_blocks)

            self.assertNotEqual(block, BlockType.HEADING)

    # Multiline clode blocks

        def test_block_to_block_code(self):
            md_blocks = "```\n Code Section```"
            block = block_to_block_type(md_blocks)

            self.assertEqual(block, BlockType.CODE)
        
        def test_block_to_block_code_2(self):
            md_blocks = "``` Code Section```"
            block = block_to_block_type(md_blocks)

            self.assertNotEqual(block, BlockType.CODE)
    
    # Quote Blocks

        def test_block_to_block_quote(self):
            md_blocks = ">Quote Section \n>Section 2"
            block = block_to_block_type(md_blocks)

            self.assertEqual(block, BlockType.QUOTE)
        
    # unordered list
        def test_block_to_block_unordered_list(self):
            md_blocks = "- line 1 \n- line 2"
            block = block_to_block_type(md_blocks)

            self.assertEqual(block, BlockType.UNORDERED_LIST)

        def test_block_to_block_unordered_list_2(self):
            md_blocks = "- line 1 \n line 2"
            block = block_to_block_type(md_blocks)

            self.assertNotEqual(block, BlockType.UNORDERED_LIST)

    # ordered list
        def test_block_to_block_ordered_list(self):
            md_blocks = "1. line 1 \n2. line 2"
            block = block_to_block_type(md_blocks)

            self.assertEqual(block, BlockType.ORDERED_LIST)

        def test_block_to_block_ordered_list_2(self):
            md_blocks = "1. line 1 \n3. line 2"
            block = block_to_block_type(md_blocks)

            self.assertNotEqual(block, BlockType.ORDERED_LIST)



if __name__ == "__main__":
    unittest.main()
