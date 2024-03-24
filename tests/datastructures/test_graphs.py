"""Unit tests for the graphs module."""

import pytest

from my_python_kata.datastructures.graphs import DEFAULT_EDGE_WEIGHT
from my_python_kata.datastructures.graphs import Edge
from my_python_kata.datastructures.graphs import GraphDefEntry
from my_python_kata.datastructures.graphs import from_list

from ..algorithms.graph_test_support import COMPLEX_GRAPH
from ..algorithms.graph_test_support import EMPTY_GRAPH
from ..algorithms.graph_test_support import ONE_NODE_GRAPH
from ..algorithms.graph_test_support import SIMPLE_GRAPH
from ..algorithms.graph_test_support import SIMPLE_GRAPH_DIRECTED
from ..algorithms.graph_test_support import TestEdge
from ..algorithms.graph_test_support import TestGraph


@pytest.mark.parametrize(
    "graph,expected_size",
    [
        (EMPTY_GRAPH, 0),
        (ONE_NODE_GRAPH, 1),
        (SIMPLE_GRAPH, 4),
        (SIMPLE_GRAPH_DIRECTED, 4),
        (COMPLEX_GRAPH, 12),
    ],
)
def test_size(graph: TestGraph, expected_size: int) -> None:
    """Test size()."""
    assert graph.size() == expected_size


@pytest.mark.parametrize(
    "graph,source,target,expected_is_connected",
    [
        (COMPLEX_GRAPH, "0", "7", True),
        (COMPLEX_GRAPH, "0", "9", True),
        (COMPLEX_GRAPH, "0", "11", True),
        (COMPLEX_GRAPH, "9", "0", True),  # Reverse
        # Corner cases
        (COMPLEX_GRAPH, "0", "0", False),  # A node is not connected to itself
        # Unexisting source and/or target nodes
        (COMPLEX_GRAPH, "not-existing", "0", False),
        (COMPLEX_GRAPH, "0", "not-existing", False),
        (COMPLEX_GRAPH, "not-existing", "not-existing", False),
        # Directed graphs don't have the reverse link between source and target nodes
        (SIMPLE_GRAPH_DIRECTED, "0", "1", True),
        (SIMPLE_GRAPH_DIRECTED, "1", "0", False),
    ],
)
def test_is_edge_present(
    graph: TestGraph, source: str, target: str, expected_is_connected: bool
) -> None:
    """Ensure that is_arc_present() function is correct."""
    assert graph.is_edge_present(source, target) == expected_is_connected


@pytest.mark.parametrize(
    "graph,source,expected_connected_nodes",
    [
        (COMPLEX_GRAPH, "0", ["7", "9", "11"]),
        (COMPLEX_GRAPH, "9", ["0", "10", "8"]),
        (COMPLEX_GRAPH, "4", ["3"]),
        (COMPLEX_GRAPH, "not-existing", []),
    ],
)
def test_get_connected_nodes(
    graph: TestGraph, source: str, expected_connected_nodes: list[str]
) -> None:
    """Test that get_connected_nodes() function returns that expected nodes."""
    assert graph.get_connected_nodes(source) == expected_connected_nodes


@pytest.mark.parametrize(
    "graph,node,expected_contained",
    [
        (COMPLEX_GRAPH, "0", True),
        (COMPLEX_GRAPH, "not-present", False),
    ],
)
def test_contains(graph: TestGraph, node: str, expected_contained: bool) -> None:
    """Check that contains() function is correct."""
    assert graph.contains(node) == expected_contained


EdgeWithWeight = tuple[TestEdge, float]


@pytest.mark.parametrize(
    "source,target,weight,bidirectional,expected_edges",
    [
        (
            "0",
            "1",
            DEFAULT_EDGE_WEIGHT,
            True,
            [
                (Edge("0", "1"), DEFAULT_EDGE_WEIGHT),
                (Edge("1", "0"), DEFAULT_EDGE_WEIGHT),
            ],
        ),
        ("0", "1", DEFAULT_EDGE_WEIGHT, False, [(Edge("0", "1"), DEFAULT_EDGE_WEIGHT)]),
        ("0", "1", 100.0, False, [(Edge("0", "1"), 100.0)]),
    ],
)
def test_connect(
    source: str,
    target: str,
    weight: float,
    bidirectional: bool,
    expected_edges: list[EdgeWithWeight],
) -> None:
    graph = TestGraph()

    graph.connect(source, target, weight, bidirectional)

    for edge_with_weight in expected_edges:
        assert graph._edges_weight[edge_with_weight[0]] == edge_with_weight[1]


def test_set_value() -> None:
    graph = ONE_NODE_GRAPH

    graph.set_data("0", "test_data")

    assert graph._nodes_data["0"] == "test_data"

    graph.set_data("0", None)

    assert "0" not in graph._nodes_data

    graph.set_data("not-present", None)
    assert "not-present" not in graph._nodes_data


def test_get_value() -> None:
    graph = ONE_NODE_GRAPH
    graph.set_data("0", "test_data")

    assert graph.get_data("0") == "test_data"


@pytest.mark.parametrize(
    "entries,expected_edges",
    [
        ([], []),
        ([("a")], []),
        ([("a", "b")], [(TestEdge("a", "b"), DEFAULT_EDGE_WEIGHT)]),
        (
            [
                ("a", "b"),
                ("a", "c"),
                ("c", "d"),
            ],
            [
                (TestEdge("a", "b"), DEFAULT_EDGE_WEIGHT),
                (TestEdge("a", "c"), DEFAULT_EDGE_WEIGHT),
                (TestEdge("c", "d"), DEFAULT_EDGE_WEIGHT),
            ],
        ),
        # You can have two edges connecting the same node pair
        # (bidirectionality)
        (
            [("a", "b"), ("b", "a")],
            [
                (TestEdge("a", "b"), DEFAULT_EDGE_WEIGHT),
                (TestEdge("b", "a"), DEFAULT_EDGE_WEIGHT),
            ],
        ),
    ],
)
def test_from_list(
    entries: list[GraphDefEntry[str]], expected_edges: list[tuple[TestEdge, float]]
) -> None:
    """Integration test list for creating a new graph from a list."""
    graph: TestGraph = from_list(entries)

    for expected_edge in expected_edges:
        expected_edge_key = expected_edge[0]
        expected_edge_weight = expected_edge[1]
        assert expected_edge_key in graph._edges_weight
        assert graph._edges_weight[expected_edge_key] == expected_edge_weight
