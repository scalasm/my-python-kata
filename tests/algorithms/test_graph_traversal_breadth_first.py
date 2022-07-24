"""Unit tests for graph Breadth-First graph traversal."""
from typing import Set

import pytest

from my_python_kata.algorithms.graph_traversal import bft
from my_python_kata.datastructures.graphs import Graph

from ..shared.graph_test_support import COMPLEX_GRAPH
from ..shared.graph_test_support import EMPTY_GRAPH
from ..shared.graph_test_support import ONE_NODE_GRAPH
from ..shared.graph_test_support import SIMPLE_GRAPH


test_bft_data = [
    (EMPTY_GRAPH, "0", True, set()),
    (ONE_NODE_GRAPH, "0", True, {"0"}),
    (ONE_NODE_GRAPH, "not-present", True, set()),
    (SIMPLE_GRAPH, "0", True, {"0", "1", "2", "3"}),
    (SIMPLE_GRAPH, "1", True, {"0", "1", "2", "3"}),
    (SIMPLE_GRAPH, "2", True, {"0", "1", "2", "3"}),
    (SIMPLE_GRAPH, "3", True, {"0", "1", "2", "3"}),
    (
        COMPLEX_GRAPH,
        "2",
        True,
        {"0", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"},
    ),
    # stop conditions
    (SIMPLE_GRAPH, "0", False, {"0"}),
]


# We ensure that we navigate all nodes
@pytest.mark.parametrize(
    "graph,start_node,action_return_value,expected_visited_nodes", test_bft_data
)
def test_bft(
    graph: Graph[str],
    start_node: str,
    action_return_value: bool,
    expected_visited_nodes: Set[str],
) -> None:
    """Test that Breadth-First Search works correctly."""
    visited_nodes: Set[str] = set()

    def track_node(node: str) -> bool:
        visited_nodes.add(node)
        return action_return_value

    bft(graph, start_node, track_node)

    assert visited_nodes == expected_visited_nodes
