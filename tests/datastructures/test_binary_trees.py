"""Unit tests for binary_trees module."""
from typing import Callable
from typing import List
from typing import Optional

import pytest

from .binary_trees_test_support import EMPTY_BINARY_TREE
from .binary_trees_test_support import SINGLE_NODE_BINARY_TREE
from .binary_trees_test_support import TestNode
from .binary_trees_test_support import THREE_NODES_BINARY_TREE
from my_python_kata.datastructures.binary_trees import ActionCallback
from my_python_kata.datastructures.binary_trees import is_empty
from my_python_kata.datastructures.binary_trees import visit_in_order
from my_python_kata.datastructures.binary_trees import visit_post_order
from my_python_kata.datastructures.binary_trees import visit_pre_order

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
def test_binary_tree_is_empty(tree: TestNode | None, expected_is_empty: bool) -> None:
    """Test that is_empty() is correct."""
    assert is_empty(tree) == expected_is_empty


# Just a shortcut for improving readability
VisitFunctionType = Callable[[Optional[TestNode], ActionCallback[str, str]], None]

test_in_order_visit_data = [
    (visit_in_order, EMPTY_BINARY_TREE, []),
    (visit_in_order, SINGLE_NODE_BINARY_TREE, ["root"]),
    (visit_in_order, THREE_NODES_BINARY_TREE, ["left", "root", "right"]),
    (visit_pre_order, EMPTY_BINARY_TREE, []),
    (visit_pre_order, SINGLE_NODE_BINARY_TREE, ["root"]),
    (visit_pre_order, THREE_NODES_BINARY_TREE, ["root", "left", "right"]),
    (visit_post_order, EMPTY_BINARY_TREE, []),
    (visit_post_order, SINGLE_NODE_BINARY_TREE, ["root"]),
    (visit_post_order, THREE_NODES_BINARY_TREE, ["left", "right", "root"]),
]


@pytest.mark.parametrize(
    "visit_function,tree_root_node,expected_visited_items", test_in_order_visit_data
)
def test_inorder_visit(
    visit_function: VisitFunctionType,
    tree_root_node: TestNode | None,
    expected_visited_items: List[str],
) -> None:
    """Ensure that we can visit the nodes and its child correctly."""
    collected_nodes: List[str] = []

    def collect(node: TestNode) -> bool:
        collected_nodes.append(node.key)
        return True

    visit_function(tree_root_node, collect)

    assert collected_nodes == expected_visited_items
