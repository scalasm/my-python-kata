"""Unit tests for binary_trees module."""
from typing import Callable
from typing import List
from typing import Optional
from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

from .binary_trees_test_support import EMPTY_BINARY_TREE
from .binary_trees_test_support import SINGLE_NODE_BINARY_TREE
from .binary_trees_test_support import TestBinaryTree
from .binary_trees_test_support import TestNode
from .binary_trees_test_support import THREE_NODES_BINARY_TREE
from interviews.datastructures.binary_trees import _visit_in_order
from interviews.datastructures.binary_trees import _visit_post_order
from interviews.datastructures.binary_trees import _visit_pre_order
from interviews.datastructures.binary_trees import ActionCallback

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


# Just a shortcut for improving readability
VisitFunctionType = Callable[[Optional[TestNode], ActionCallback[str, str]], None]

test_in_order_visit_data = [
    (_visit_in_order, EMPTY_BINARY_TREE.root, []),
    (_visit_in_order, SINGLE_NODE_BINARY_TREE.root, ["root"]),
    (_visit_in_order, THREE_NODES_BINARY_TREE.root, ["left", "root", "right"]),
    (_visit_pre_order, EMPTY_BINARY_TREE.root, []),
    (_visit_pre_order, SINGLE_NODE_BINARY_TREE.root, ["root"]),
    (_visit_pre_order, THREE_NODES_BINARY_TREE.root, ["root", "left", "right"]),
    (_visit_post_order, EMPTY_BINARY_TREE.root, []),
    (_visit_post_order, SINGLE_NODE_BINARY_TREE.root, ["root"]),
    (_visit_post_order, THREE_NODES_BINARY_TREE.root, ["left", "right", "root"]),
]


@pytest.mark.parametrize(
    "visit_function,tree_root_node,expected_visited_items", test_in_order_visit_data
)
def test_inorder_visit(
    visit_function: VisitFunctionType,
    tree_root_node: TestNode,
    expected_visited_items: List[str],
) -> None:
    """Ensure that we can visit the nodes and its child correctly."""
    collected_nodes: List[str] = []

    def collect(node: TestNode) -> bool:
        collected_nodes.append(node.key)
        return True

    visit_function(tree_root_node, collect)

    assert collected_nodes == expected_visited_items


test_binary_tree_inorder_visit_data = [
    (EMPTY_BINARY_TREE, 1),
    (SINGLE_NODE_BINARY_TREE, 1),
    (THREE_NODES_BINARY_TREE, 1),
]


# The _visit_in_order() and similar functions are mocked in these tests.
# Yet, we want to be sure to call it once to just start visiting the tree.


@pytest.fixture
def mock_visit_in_order(
    mocker: MockerFixture,
) -> Mock:
    """Provides a mock for the _visit_in_order() function."""
    return mocker.patch(
        "interviews.datastructures.binary_trees._visit_in_order", return_value=None
    )


@pytest.mark.parametrize(
    "tree,expected_num_visit_calls", test_binary_tree_inorder_visit_data
)
def test_binary_tree_in_order_visit(
    tree: TestBinaryTree,
    expected_num_visit_calls: int,
    mock_visit_in_order: Mock,
) -> None:
    """Verify that we call the _visit_in_order function."""

    def do_nothing(_: TestNode) -> bool:
        pass

    tree.visit_in_order(do_nothing)

    assert mock_visit_in_order.call_count == expected_num_visit_calls


@pytest.fixture
def mock_visit_pre_order(
    mocker: MockerFixture,
) -> Mock:
    """Provides a mock for the _visit_pre_order() function."""
    return mocker.patch(
        "interviews.datastructures.binary_trees._visit_pre_order", return_value=None
    )


@pytest.mark.parametrize(
    "tree,expected_num_visit_calls", test_binary_tree_inorder_visit_data
)
def test_binary_tree_pre_order_visit(
    tree: TestBinaryTree,
    expected_num_visit_calls: int,
    mock_visit_pre_order: Mock,
) -> None:
    """Verify that we call the mock_visit_pre_order function."""

    def do_nothing(_: TestNode) -> bool:
        pass

    tree.visit_pre_order(do_nothing)

    assert mock_visit_pre_order.call_count == expected_num_visit_calls


@pytest.fixture
def mock_visit_post_order(
    mocker: MockerFixture,
) -> Mock:
    """Provides a mock for the _visit_post_order() function."""
    return mocker.patch(
        "interviews.datastructures.binary_trees._visit_post_order", return_value=None
    )


@pytest.mark.parametrize(
    "tree,expected_num_visit_calls", test_binary_tree_inorder_visit_data
)
def test_binary_tree_post_order_visit(
    tree: TestBinaryTree,
    expected_num_visit_calls: int,
    mock_visit_post_order: Mock,
) -> None:
    """Verify that we call the mock_visit_post_order function."""

    def do_nothing(_: TestNode) -> bool:
        pass

    tree.visit_post_order(do_nothing)

    assert mock_visit_post_order.call_count == expected_num_visit_calls
