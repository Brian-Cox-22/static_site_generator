import re

def extract_markdown_images(text):
    '''
    Takes raw markdown text, returns a list of touples
    Touple contains alt text and url of image
    '''

    alt_text = re.findall(r"\[([^\[\]]*)\]", text)
    url = re.findall(r"\(([^\(\)]*)\)", text)

    lst = []

    for i in range(len(alt_text)):
        toup = (alt_text[i], url[i])
        lst.append(toup)

    return lst

def extract_markdown_link(text):

    alt_text = re.findall(r"(?<!!)\[([^\[\]]*)\]", text)
    url = re.findall(r"\(([^\(\)]*)\)", text)

    lst = []

    for i in range(len(alt_text)):
        toup = (alt_text[i], url[i])
        lst.append(toup)

    return lst