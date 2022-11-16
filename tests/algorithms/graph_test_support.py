"""Shared test resources for testing graphs and related traversal algorithms."""
from my_python_kata.datastructures.graphs import Edge
from my_python_kata.datastructures.graphs import Graph
from my_python_kata.datastructures.graphs import from_list


TestGraph = Graph[str, str]
TestEdge = Edge[str]


def _create_empty_graph() -> TestGraph:
    return TestGraph()


def _create_one_node_graph() -> TestGraph:
    # Disabled MyPy check because of https://github.com/python/mypy/issues/1178
    return from_list([("0")])  # type: ignore[list-item]


def _create_simple_graph() -> TestGraph:
    return from_list(
        [
            ("0", "1"),
            ("0", "2"),
            ("0", "3"),
        ]
    )


def _create_simple_graph_directed() -> TestGraph:
    return from_list(
        [
            ("0", "1", 1.0, False),
            ("0", "2", 1.0, False),
            ("0", "3", 1.0, False),
        ]
    )


def _create_complex_graph() -> TestGraph:
    return from_list(
        [
            ("0", "7"),
            ("0", "9"),
            ("0", "11"),
            ("9", "10"),
            ("9", "8"),
            ("8", "12"),
            ("12", "2"),
            ("7", "11"),
            ("7", "6"),
            ("3", "2"),
            ("3", "4"),
            ("6", "5"),
        ]
    )


EMPTY_GRAPH = _create_empty_graph()

ONE_NODE_GRAPH = _create_one_node_graph()

SIMPLE_GRAPH = _create_simple_graph()

SIMPLE_GRAPH_DIRECTED = _create_simple_graph_directed()

COMPLEX_GRAPH = _create_complex_graph()
