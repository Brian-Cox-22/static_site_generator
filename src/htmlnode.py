
class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        '''
        tag - string of tag name  (e.g. "p", "a", "h1", etc.)
        value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        children - A list of HTMLNode objects representing the children of this node
        props - A dictionary of key-value pairs representing the attributes of the HTML tag 
        '''
        self.tag = tag # string tag name
        self.value = value # string representing the text
        self.children = children # list of HTMLNode objects representing the children of the node
        self.props = props # dictionary of key-value pairs 

    def to_html(self):
        raise Exception(NotImplementedError)
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        return (f"Tag = {self.tag},\n value = {self.value},\n children = {self.children},\n props = {self.props}")