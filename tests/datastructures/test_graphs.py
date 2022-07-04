"""Unit tests for the graphs module."""
from typing import Any
from typing import List

import pytest

from my_python_kata.datastructures.graphs import Graph

from ..algorithms.graph_test_support import COMPLEX_GRAPH
from ..algorithms.graph_test_support import SIMPLE_GRAPH_DIRECTED


test_size_data = [(["a", []], 1), (["a", ["b", "c"]], 3)]


@pytest.mark.parametrize("data,expected_size", test_size_data)
def test_size(data: List[Any], expected_size: int) -> None:
    """Test size()."""
    graph = Graph[str]()

    source_item: str = data[0]
    target_items: List[str] = data[1]

    graph.connect(source_item, target_items)

    assert graph.size() == expected_size


test_connect_data = [
    (COMPLEX_GRAPH, "0", "7", True),
    (COMPLEX_GRAPH, "0", "9", True),
    (COMPLEX_GRAPH, "0", "11", True),
    (COMPLEX_GRAPH, "9", "0", True),  # Reverse
    # Corner cases
    (COMPLEX_GRAPH, "0", "0", False),  # A node is not connected to itself
    (COMPLEX_GRAPH, None, "7", False),
    (COMPLEX_GRAPH, "0", None, False),
    (COMPLEX_GRAPH, False, None, False),
    # Unexisting source and/or target nodes
    (COMPLEX_GRAPH, "not-existing", "0", False),
    (COMPLEX_GRAPH, "0", "not-existing", False),
    (COMPLEX_GRAPH, "not-existing", "not-existing", False),
    # Directed graphs don't have the reverse link between source and target nodes
    (SIMPLE_GRAPH_DIRECTED, "0", "1", True),
    (SIMPLE_GRAPH_DIRECTED, "1", "0", False),
]


@pytest.mark.parametrize("graph,source,target,expected_is_connected", test_connect_data)
def test_connect(
    graph: Graph[str], source: str, target: str, expected_is_connected: bool
) -> None:
    """Ensure that is_arc_present() function is correct."""
    assert graph.is_arc_present(source, target) == expected_is_connected


test_get_connected_nodes_data = [
    (COMPLEX_GRAPH, "0", ["7", "9", "11"]),
    (COMPLEX_GRAPH, "9", ["0", "10", "8"]),
    (COMPLEX_GRAPH, "4", ["3"]),
    (COMPLEX_GRAPH, "not-existing", []),
]


@pytest.mark.parametrize(
    "graph,source,expected_connected_nodes", test_get_connected_nodes_data
)
def test_get_connected_nodes(
    graph: Graph[str], source: str, expected_connected_nodes: List[str]
) -> None:
    """Test that get_connected_nodes() function returns that expected nodes."""
    assert graph.get_connected_nodes(source) == expected_connected_nodes


test_contains_data = [
    (COMPLEX_GRAPH, "0", True),
    (COMPLEX_GRAPH, "not-present", False),
]


@pytest.mark.parametrize("graph,node,expected_contained", test_contains_data)
def test_contains(graph: Graph[str], node: str, expected_contained: bool) -> None:
    """Check that contains() function is correct."""
    assert graph.contains(node) == expected_contained
