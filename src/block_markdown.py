from enum import Enum


def markdown_to_blocks(markdown: str):
    '''
    Takes a raw markdown string (full document) as input
    Returns a list of block strings
    Assumes that each block will be seperated by a blank line
    '''

    # split based on \n\n
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

class BlockType(Enum):
    '''
    Creates Enums for:
        paragraph
        heading
        code
        quote
        unordered_list
        ordered_lis
    '''

    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown_block):
    '''
    Goal is to identify the ENUM that each block is. Blocks come in stripped from markdown_to_blocks
    '''

    # headings — 1-6 # + a space
    if markdown_block.startswith(("# ","## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    

    elif markdown_block.startswith(">"):
        lines = markdown_block.split("\n")
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    

    elif markdown_block.startswith("- "):
        lines = markdown_block.split("\n")
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    

    elif markdown_block.startswith("1. "):
        order = 1
        lines = markdown_block.split("\n")
        for line in lines:
            if not line.startswith(f"{order}. "):
                return BlockType.PARAGRAPH
            order += 1
        return BlockType.ORDERED_LIST
    

    elif markdown_block.startswith("```\n") and len(markdown_block.split("\n")) >=2 and markdown_block.endswith("```"):
        return BlockType.CODE
    

    else:
        return BlockType.PARAGRAPH