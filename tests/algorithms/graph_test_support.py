"""
Shared test resources for testing graphs and related traversal algorithms.
"""
from interviews.datastructures.graphs import Graph


def _create_empty_graph() -> Graph[str]:
    return Graph[str]()


def _create_one_node_graph() -> Graph[str]:
    graph = Graph[str]()

    graph.connect("0", [])

    return graph


def _create_simple_graph() -> Graph[str]:
    graph = Graph[str]()

    graph.connect("0", ["1", "2", "3"])

    return graph


def _create_simple_graph_directed() -> Graph[str]:
    graph = Graph[str]()

    graph.connect("0", ["1", "2", "3"], bidirectional=False)

    return graph


def _create_complex_graph() -> Graph[str]:
    graph = Graph[str]()

    graph.connect("0", ["7", "9", "11"])
    graph.connect("9", ["10", "8"])
    graph.connect("9", ["10", "8"])
    graph.connect("8", ["12"])
    graph.connect("12", ["2"])
    graph.connect("7", ["11", "6"])
    graph.connect("3", ["2", "4"])
    graph.connect("6", ["5"])

    return graph


EMPTY_GRAPH = _create_empty_graph()

ONE_NODE_GRAPH = _create_one_node_graph()

SIMPLE_GRAPH = _create_simple_graph()

SIMPLE_GRAPH_DIRECTED = _create_simple_graph_directed()

COMPLEX_GRAPH = _create_complex_graph()
