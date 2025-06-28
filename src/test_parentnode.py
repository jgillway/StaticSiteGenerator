import unittest
from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_multiple_children(self):
        n1 = LeafNode("b", "Bold")
        n2 = LeafNode(None, " and ")
        n3 = LeafNode("i", "Italic")
        parent = ParentNode("p", [n1, n2, n3])
        self.assertEqual(parent.to_html(), "<p><b>Bold</b> and <i>Italic</i></p>")

    def test_to_html_nested_parents(self):
        inner = ParentNode("span", [LeafNode(None, "inner")])
        outer = ParentNode("div", [inner, LeafNode(None, " outer")])
        self.assertEqual(outer.to_html(), "<div><span>inner</span> outer</div>")

    def test_to_html_with_props(self):
        child = LeafNode("b", "bold")
        parent = ParentNode("div", [child], {"class": "container"})
        self.assertEqual(parent.to_html(), '<div class="container"><b>bold</b></div>')

    def test_to_html_raises_no_tag(self):
        child = LeafNode("b", "bold")
        with self.assertRaises(ValueError):
            ParentNode(None, [child]).to_html()

    def test_to_html_raises_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()

if __name__ == "__main__":
    unittest.main()
