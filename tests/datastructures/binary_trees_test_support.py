"""Test support for binary trees."""
from interviews.datastructures.binary_trees import BinaryTree
from interviews.datastructures.binary_trees import Node

TestNode = Node[str, str]
TestBinaryTree = BinaryTree[str, str]


def _create_empty_binary_tree() -> TestBinaryTree:
    return TestBinaryTree()


def _create_single_node_binary_tree() -> TestBinaryTree:
    return TestBinaryTree(TestNode("root", "root_value"))


def _create_3_nodes_balanced_binary_tree() -> TestBinaryTree:
    root = TestNode("root", "root_value")
    root.left_child = TestNode("left", "left_value")
    root.right_child = TestNode("right", "right_value")

    return TestBinaryTree(root)


EMPTY_BINARY_TREE = _create_empty_binary_tree()

SINGLE_NODE_BINARY_TREE = _create_single_node_binary_tree()

THREE_NODES_BINARY_TREE = _create_3_nodes_balanced_binary_tree()
