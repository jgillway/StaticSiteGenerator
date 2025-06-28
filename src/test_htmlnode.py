import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "Content", [], {"class": "test"})
        node2 = HTMLNode("div", "Content", [], {"class": "test"})
        self.assertEqual(node, node2)

    def test_neq(self):
        node = HTMLNode("div", "Content", [], {"class": "test"})
        node2 = HTMLNode("span", "Content", [], {"class": "test"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("div", "Content", [], {"class": "test", "id": "unique"})
        self.assertEqual(node.props_to_html(), 'class="test" id="unique"')

    def test_props_to_html_empty(self):
        node = HTMLNode("div", "Content", [])
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("div", "Content", [], {"class": "test"})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Content, children=[], props={'class': 'test'})")

    def test_to_html_not_implemented(self):
        node = HTMLNode("div", "Content")
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()