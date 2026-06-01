from htmlnode import HTMLNode, LeafNode, ParentNode
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from textnode import text_node_to_html_node, TextNode, TextType
from inline_markdown import text_to_textnodes

# split into markdown blocks
def markdown_to_html_node(markdown):
    '''
    Converts a whole document into a single parent HTMLNode
    '''
    blocks = markdown_to_blocks(markdown)

    nodes_list = []
    for block in blocks:
        new_node = create_html_node_block(block)
        nodes_list.append(new_node)
    
    # create wrapper parent node
    
    return ParentNode(tag="div", children = nodes_list)



# building the parent node
def create_html_node_block(block) -> HTMLNode:

    tag_text = determine_block_tag(block)
    # print(tag_text[0])
    # print(repr(block))

    if tag_text[0] == "code":
        txt_nd = TextNode(text=block.removeprefix("```\n").removesuffix("```"), text_type=TextType.TEXT)
        leaf = text_node_to_html_node(txt_nd)

        p1 = ParentNode(tag = "code", children= [leaf])
        parent_node = ParentNode(tag = "pre", children=[p1])
    
    elif tag_text[0] == "ul":
        lines = block.split("\n")
        new_lines = []
        for line in lines:
            new = line.removeprefix("- ")
            new_lines.append(ParentNode("li", text_to_children(new)))
        parent_node = ParentNode("ul", new_lines)
        
    elif tag_text[0] == "ol":
        lines = block.split("\n")
        new_lines = []
        
        for line in lines:
            char_remove = line.find(".") + 2
            new = line[char_remove:]
            new_lines.append(ParentNode("li", text_to_children(new)))
        parent_node = ParentNode("ol", new_lines)
    
    else:
        parent_node = ParentNode(tag = tag_text[0], children=text_to_children(tag_text[1]))

    
    return parent_node


def determine_block_tag(block):
    BlockType_lib = {BlockType.PARAGRAPH:"p", BlockType.HEADING:"h", BlockType.CODE:"code",
                      BlockType.UNORDERED_LIST:"ul", BlockType.ORDERED_LIST:"ol", BlockType.QUOTE:"blockquote"}

    block_type = block_to_block_type(block)
    output_text = block

    tag = BlockType_lib[block_type]
    if block_type == BlockType.HEADING:
        num_pound = 0
        for char in block:
            if char == "#":
                num_pound += 1
            else:
                break
        
        tag = f"h{num_pound}"
        output_text = block[num_pound:]
    
    elif block_type == BlockType.PARAGRAPH:
        txt = block.split("\n")
        join = " ".join(txt)
        output_text = join

    elif block_type == BlockType.ORDERED_LIST:
        pass
    
    else:
        tag = BlockType_lib[block_type]
    
    return tag, output_text


# identifying the children blocks
def text_to_children(text: str):
    '''
    Takes a string of text and returns a list of HTMLNodes representing inline markeown
    '''
    
    text_nodes = text_to_textnodes(text)

    leaf_nodes = []
    for txt in text_nodes:
        leaf_nodes.append(text_node_to_html_node(txt))

    return leaf_nodes
    
