"""Unit tests for binary_trees module."""
import pytest

from .binary_trees_test_support import EMPTY_BINARY_TREE
from .binary_trees_test_support import SINGLE_NODE_BINARY_TREE
from .binary_trees_test_support import TestBinaryTree
from .binary_trees_test_support import TestNode
from .binary_trees_test_support import THREE_NODES_BINARY_TREE

test_create_node_data = [
    (TestNode("k1", "v1"), "k1", "v1"),
    (TestNode("k1"), "k1", None),
]


@pytest.mark.parametrize("node,expected_key,expected_value", test_create_node_data)
def test_create_node(node: TestNode, expected_key: str, expected_value: str) -> None:
    """Test that we can create nodes correctly."""

    assert node.key == expected_key
    assert node.value == expected_value


test_can_change_value_data = [
    (TestNode("k1", "v1"), "v2"),
    (TestNode("k1", "v1"), None),
]


@pytest.mark.parametrize("node,expected_new_value", test_can_change_value_data)
def test_can_change_value(node: TestNode, expected_new_value: str) -> None:
    """Test that we can actually change the value for a node."""
    node.value = expected_new_value

    assert node.value == expected_new_value


test_binary_tree_is_empty_data = [
    (EMPTY_BINARY_TREE, True),
    (SINGLE_NODE_BINARY_TREE, False),
    (THREE_NODES_BINARY_TREE, False),
]


@pytest.mark.parametrize("tree,expected_is_empty", test_binary_tree_is_empty_data)
def test_binary_tree_is_empty(tree: TestBinaryTree, expected_is_empty: bool) -> None:
    """Test that is_empty() is correct."""
    assert tree.is_empty() == expected_is_empty
