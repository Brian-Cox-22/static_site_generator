import re

from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    '''
    only for text types
    old_nodes - list of nodes
    deliminator
    text_type - the type of text
    '''
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    '''
    similar to split node deliminator, but only on images
    '''
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []

        images = extract_markdown_images(old_node.text)
        original_text = old_node.text
        if len(images) == 0:
            split_nodes.append(old_node)
            new_nodes.extend(split_nodes)
            continue
        for image in images:
            marker = f"![{image[0]}]({image[1]})"
            sections = original_text.split(marker, maxsplit = 1)
            if len(sections) != 2:
                 raise ValueError("invalid markdown, image section not closed")
            
            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            split_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            
            original_text = sections[1]
        
        if original_text:
            split_nodes.append(TextNode(original_text, TextType.TEXT))
            
        new_nodes.extend(split_nodes)
    return new_nodes



def split_nodes_link(old_nodes):
    '''
    similar to split node deliminator, but only on links (basically same as images)
    '''
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []

        links = extract_markdown_links(old_node.text)
        original_text = old_node.text
        if len(links) == 0:
            split_nodes.append(old_node)
            new_nodes.extend(split_nodes)
            continue
        for link in links:
            marker = f"[{link[0]}]({link[1]})"
            sections = original_text.split(marker, maxsplit = 1)
            if len(sections) != 2:
                 raise ValueError("invalid markdown, link section not closed")
            
            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            split_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            
            original_text = sections[1]
        
        if original_text:
            split_nodes.append(TextNode(original_text, TextType.TEXT))
            
        new_nodes.extend(split_nodes)
    return new_nodes