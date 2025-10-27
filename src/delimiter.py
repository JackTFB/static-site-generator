from src.textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    delimiters = {
        "**": TextType.BOLD,
        "_": TextType.ITALIC,
        "`": TextType.CODE
    }
    new_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        elif delimiter not in delimiters and text_type != delimiters[delimiter]:
            raise Exception("Invalid delimiter/text type")
        else:
            node_text = node.text
            if delimiter not in node_text:
                new_nodes.append(node)
            string_list = node_text.split(delimiter)
            if len(string_list) % 2 == 0:
                raise Exception("Invalid Markdown syntax")
            else:
                for i in range(len(string_list)):
                    if i % 2:
                        new_nodes.append(TextNode(string_list[i], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(string_list[i], text_type))

    return new_nodes