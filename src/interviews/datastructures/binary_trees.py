"""Binary trees."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable
from typing import Generic
from typing import TypeVar

# Key type, we only support int or strings (easier for our implementation)
K = TypeVar("K", int, str)

# Value type, could be anything
V = TypeVar("V")


@dataclass
class Node(Generic[K, V]):
    """A single node in a binary tree.

    Key is immutable while value can be changed, eventually set to None.
    """

    __slots__ = ["_key", "value", "left_child", "right_child"]

    _key: K
    value: V | None

    left_child: Node[K, V] | None
    right_child: Node[K, V] | None

    def __init__(
        self,
        key: K,
        value: V | None = None,
        left_child: Node[K, V] | None = None,
        right_child: Node[K, V] | None = None,
    ) -> None:
        """Build a new node.

        Args:
            key: the key for this node
            value: the value of this node (optional)
            left_child: the left node (optional)
            right_child: the right node (optional)
        """
        self._key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    @property
    def key(self) -> K:
        """Returns the key for this node."""
        return self._key


# Alias for better readability
ActionCallback = Callable[[Node[K, V]], bool]


def _visit_in_order(
    node: Node[K, V] | None, on_node_action: ActionCallback[K, V]
) -> None:
    """Visit a tree using in-order strategy.

    See https://en.wikipedia.org/wiki/Tree_traversal.
    """
    if not node:
        return

    _visit_in_order(node.left_child, on_node_action)

    on_node_action(node)

    _visit_in_order(node.right_child, on_node_action)


def _visit_pre_order(
    node: Node[K, V] | None, on_node_action: ActionCallback[K, V]
) -> None:
    """Visit a tree using pre-order strategy.

    See https://en.wikipedia.org/wiki/Tree_traversal.
    """
    if not node:
        return

    on_node_action(node)

    _visit_in_order(node.left_child, on_node_action)

    _visit_in_order(node.right_child, on_node_action)


def _visit_post_order(
    node: Node[K, V] | None, on_node_action: ActionCallback[K, V]
) -> None:
    """Visit a tree using post-order strategy.

    See https://en.wikipedia.org/wiki/Tree_traversal.
    """
    if not node:
        return

    _visit_in_order(node.left_child, on_node_action)

    _visit_in_order(node.right_child, on_node_action)

    on_node_action(node)


@dataclass
class BinaryTree(Generic[K, V]):
    """A Binary tree."""

    root: Node[K, V] | None = None

    def __init__(self, root: Node[K, V] | None = None) -> None:
        """Creaste a new empty binary tree.

        Args:
            root: the optional root for this tree
        """
        self.root = root

    def is_empty(self) -> bool:
        """Checks that this binary tree has at least one node."""
        return self.root is None

    def visit_in_order(self, on_node_action: ActionCallback[K, V]) -> None:
        """Visit a tree in order.

        Args:
            on_node_action: callback invoked for each node
        """
        _visit_in_order(self.root, on_node_action)

    def visit_pre_order(self, on_node_action: ActionCallback[K, V]) -> None:
        """Visit a tree in pre-order.

        Args:
            on_node_action: callback invoked for each node
        """
        _visit_pre_order(self.root, on_node_action)

    def visit_post_order(self, on_node_action: ActionCallback[K, V]) -> None:
        """Visit a tree in post-order.

        Args:
            on_node_action: callback invoked for each node
        """
        _visit_post_order(self.root, on_node_action)
