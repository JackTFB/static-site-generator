import unittest

from delimiter import split_nodes_delimiter
from src.textnode import TextNode, TextType


class TestSplitText(unittest.TestCase):
    def test_split(self):
        print("Testing split text function")
        nodes = [
            TextNode("Here is some text", TextType.TEXT),
            TextNode("Here is some **BOLD** text", TextType.BOLD),
            TextNode("Here is some _fancy_ text", TextType.ITALIC),
            TextNode("Here is some `code`", TextType.CODE)
        ]
        split_nodes_delimiter(nodes, "**", TextType.BOLD)
        split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        output = split_nodes_delimiter(nodes, "`", TextType.CODE)

        print("Split text function success")
