import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props(self):

        print("Test 1")
        node_props = {"height": "10", "font-family": "sans-serif"}
        node = HTMLNode("p", "This is a text node", props=node_props)
        node1 = HTMLNode("p", "This is a text node")
        self.assertNotEqual(node, node1)
        print(node.props_to_html())
        print("TEST SUCCESSFUL")

