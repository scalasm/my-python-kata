# Generic data type per items in a data page
import collections
from typing import Dict
from typing import Generic
from typing import List
from typing import TypeVar

# Generic type for the Graph class
T = TypeVar("T")


class Graph(Generic[T]):
    """
    A generic graph for tracking nodes and their connecting arcs.\n
    Implementation notes:
     * it uses adjacency lists (a dict of lists) for storing nodes and their
       connected nodes.
     * it favors runtime performannce at the expense of build time performance
       e.g., we use lists for storing nodes even if checking that there are no
       duplicates nodes at build time is more expensive that using a set.
       Using a list is more efficient when traversing the graph instead of
       using a set (you usually iterate on all connected nodes anyway).\n\n
    Note that the generic type T must respect the Comparable contract and support
    <, >, and == operators.
    """

    _nodes_by_id: Dict[T, List[T]]

    def __init__(self) -> None:
        self._nodes_by_id = collections.defaultdict(list)

    def connect(
        self, source_node: T, target_nodes: List[T], bidirectional: bool = True
    ) -> None:
        """
        Connect a not to a other nodes.

        Args:
            - source_node - the source node :)
            - target_nodes - a list of target nodes that will be connected to
              source node
            - bidirectional - a flag that indicates if the arc is going to be
              bidirectional (default: True)
        """
        connected_nodes = self._nodes_by_id[source_node]
        for target_node in target_nodes:
            if target_node not in connected_nodes:
                connected_nodes.append(target_node)

            if bidirectional:
                target_node_connected_nodes = self._nodes_by_id[target_node]
                if source_node not in target_node_connected_nodes:
                    target_node_connected_nodes.append(source_node)

    def is_arc_present(self, source_node: T, target_node: T) -> bool:
        """
        Checks if two nodes are connected, assuming a directional connection
        (that is, if "source_node --> target_node", not viceversa).

        Args:
            - source_node - the source node :)
            - target_nodes - the target node

        Returns:
            - True if there is a connection from source_node to target_node,
              False otherwise
        """
        target_nodes = self._nodes_by_id.get(source_node, None)
        if not target_nodes:
            return False

        return target_node in target_nodes

    def size(self) -> int:
        """
        Returns the amount of nodes within this graph.
        """
        return len(self._nodes_by_id)

    def get_connected_nodes(self, node: T) -> List[T]:
        """
        Returns a list of nodes if a connecting arc with this node exists.
        Result may be empty if there are no connected nodes (e.g., leaf or
        disjointed node) or there is no such node.
        """
        return self._nodes_by_id[node] if self.contains(node) else []

    def contains(self, node: T) -> bool:
        return node in self._nodes_by_id
