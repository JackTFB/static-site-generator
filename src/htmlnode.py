class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return_text = ""
        for prop in self.props:
            return_text += f"{prop}={self.props[prop]} "

        return return_text

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return f"{self.value}"

        return_text = f"<{self.tag}"

        if self.props is not None:
            for prop in self.props:
                return_text += f' {prop}="{self.props[prop]}"'

        return_text += f">{self.value}</{self.tag}>"

        return return_text

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            return ValueError("No tag value found")

        if self.children is None:
            return ValueError("No children value found")

        return_text = f"<{self.tag}"

        if self.props is not None:
            for prop in self.props:
                return_text += f' {prop}="{self.props[prop]}'

        return_text += ">"

        if len(self.children) != 0:
            for child in self.children:
                if isinstance(child, LeafNode):
                    return_text += child.to_html()
                elif isinstance(child, ParentNode):
                    return_text += child.to_html()
                elif isinstance(child, HTMLNode):
                    return_text += child.to_html()
                else:
                    return_text += str(child)

        return_text += f"</{self.tag}>"

        return return_text

