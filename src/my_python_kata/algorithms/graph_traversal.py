"""Graph traversal algorithms."""

from typing import Callable

from my_python_kata.datastructures.graphs import Graph
from my_python_kata.datastructures.graphs import K
from my_python_kata.datastructures.graphs import T


# Action callback is provided for customizing behavior when visiting nodes
GraphActionCallback = Callable[[K], bool]


def bft(
    graph: Graph[K, T], start_node: K, on_node_action: GraphActionCallback[K]
) -> None:
    """Breadt-First traversal.

    Performs Breadth-First Traversal of the given graph, starting from the
    specified node and performing the specified action.

    Callback actions must return True if they want to continue traversal or
    False if they want to stop after processing the current node.

    Args:
        graph: the graph to be processed
        start_node: the node to start traversal from
        on_node_action: a callback that will be invoked on each traversal.
    """
    if not graph.contains(start_node):
        return

    fringe_nodes: list[K] = [start_node]
    visited_nodes: set[K] = set()

    while fringe_nodes:
        current_node = fringe_nodes.pop(0)

        # We allow clients to quit the traversal, if they return False in the
        # action callback.
        # Quickest way is to clear the current fringe so nothing will happen
        if on_node_action(current_node):
            visited_nodes.add(current_node)

            for connected_node in graph.get_connected_nodes(current_node):
                if connected_node not in visited_nodes:
                    fringe_nodes.append(connected_node)
        else:
            fringe_nodes.clear()
