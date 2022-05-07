"""Test support for binary trees."""
from __future__ import annotations

from typing import Optional
from interviews.datastructures.binary_trees import Node

TestNode = Node[str, str]


def _create_empty_binary_tree() -> (TestNode | None):
    return None


def _create_single_node_binary_tree() -> TestNode:
    return TestNode("root", "root_value", None, None)


def _create_3_nodes_balanced_binary_tree() -> TestNode:
    root = TestNode("root", "root_value")
    root.left_child = TestNode("left", "left_value")
    root.right_child = TestNode("right", "right_value")

    return root


EMPTY_BINARY_TREE = _create_empty_binary_tree()

SINGLE_NODE_BINARY_TREE = _create_single_node_binary_tree()

THREE_NODES_BINARY_TREE = _create_3_nodes_balanced_binary_tree()
