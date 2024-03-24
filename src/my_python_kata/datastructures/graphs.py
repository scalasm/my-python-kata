"""Graph module implemented using adjacency lists."""

from collections import defaultdict
from dataclasses import dataclass
from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import cast


# Generic type for the Graph class
K = TypeVar("K", int, str)
T = TypeVar("T")

DEFAULT_EDGE_WEIGHT = 1.0


@dataclass(eq=True, frozen=True)
class Edge(Generic[K]):
    """An edge connects two different nodes."""

    source: K
    target: K


class Graph(Generic[K, T]):
    """A generic graph for tracking nodes and their connecting arcs.

    Implementation notes:
     * it uses adjacency lists (a dict of lists) for storing nodes and their
       connected nodes.
     * it favors runtime performannce at the expense of build time performance
       e.g., we use lists for storing nodes even if checking that there are no
       duplicates nodes at build time is more expensive that using a set.
       Using a list is more efficient when traversing the graph instead of
       using a set (you usually iterate on all connected nodes anyway).

    Note that the generic type K must respect the Comparable contract and support
    <, >, and == operators.
    """

    _nodes: dict[K, list[K]]

    _nodes_data: dict[K, T]

    _edges_weight: dict[Edge[K], float]

    def __init__(self) -> None:
        """Construct a new empty graph."""
        self._nodes = defaultdict(list)
        self._nodes_data = dict()
        self._edges_weight = dict()

    def connect(
        self,
        source_node: K,
        target_node: K,
        weight: float = DEFAULT_EDGE_WEIGHT,
        bidirectional: bool = True,
    ) -> None:
        """Connect a not to a other nodes.

        If source node is not already present, it will be added automatically.

        Args:
            source_node: the source node
            target_node: the target node to connect to
            weight: the weight to be assigned to this edge
                (default: DEFAULT_EDGE_WEIGHT)
            bidirectional: a flag that indicates if the arc is going to be
                bidirectional (default: True)
        """
        self._connect(source_node, target_node, weight)

        if bidirectional:
            self._connect(target_node, source_node, weight)

    def _connect(self, source_node: K, target_node: K, weight: float) -> None:
        connected_nodes = self._nodes[source_node]
        if target_node not in connected_nodes:
            self.add_node(target_node)

            connected_nodes.append(target_node)

            self._edges_weight[Edge(source_node, target_node)] = weight

    def is_edge_present(self, source_node: K, target_node: K) -> bool:
        """Checks if two nodes are connected, assuming a directional connection.

        This function will check if "source_node --> target_node" only.

        Args:
            source_node: the source node :)
            target_node: the target node

        Returns:
            True if there is a connection from source_node to target_node,
                False otherwise
        """
        return Edge[K](source_node, target_node) in self._edges_weight

    def size(self) -> int:
        """Returns the amount of nodes within this graph."""
        return len(self._nodes)

    def get_connected_nodes(self, node: K) -> list[K]:
        """Returns a list of nodes if a connecting arc with this node exists.

        Result may be empty if there are no connected nodes (e.g., leaf or
        disjointed node) or there is no such node.
        """
        return self._nodes[node] if self.contains(node) else []

    def contains(self, node: K) -> bool:
        """Check if the specified node is present in this graph.

        Args:
            node: the node to check for presence.

        Returns:
            True if the node is present, False otherwise
        """
        return node in self._nodes

    def add_node(self, node: K) -> None:
        """Add a single node to the graph, without any connection.

        If the node is already present, nothing will be done.

        Args:
            node: the node key
        """
        if node not in self._nodes:
            self._nodes[node] = list()

    def get_data(self, key: K) -> Optional[T]:
        """Returns the value associated to the key, if present.

        Args:
            key: the node key

        Returns:
            the value if present, or None if the node is not present or
            no value was assigned to it.
        """
        return self._nodes_data.get(key, None)

    def set_data(self, key: K, data: Optional[T]) -> None:
        """Sets the data for a given node.

        If data is None, than any pre-existing data is removed.

        Args:
            key: the target node
            data: the data to assign for that node
        """
        if data:
            self._nodes_data[key] = data
        elif key in self._nodes_data:
            del self._nodes_data[key]


# Disabled MyPy check because of
# https://github.com/python/mypy/issues/1178
GraphDefEntry = (
    tuple[K]
    | tuple[K, K]  # type: ignore[misc]
    | tuple[K, K, float]  # type: ignore[misc]
    | tuple[K, K, float, bool]  # type: ignore[misc]
)


def from_list(entries: list[GraphDefEntry[K]]) -> Graph[K, T]:
    """Factory for creating a new graph from a list of tuples.

    Each entry can be:
     * single node only
     * (source, target) only tuple
     * (source, target, weight)
     * (source, target, weight, bidirectional)

    Unless otherwise specified, all edges are bidirectional and have
    DEFAULT_EDGE_WEIGHT .

    Args:
        entries: a list of GraphDefEntry tuples

    Returns:
        the graph
    """
    graph = Graph[K, T]()

    for entry in entries:
        n_parameters = len(entry)

        if n_parameters == 1:
            source_node: K = entry[0]
            graph.add_node(source_node)
        else:
            source_node = entry[0]
            # Disabled MyPy check because of
            # https://github.com/python/mypy/issues/1178
            target_node = entry[1]  # type: ignore[misc]

            edge_weight = (
                cast(float, entry[2])  # type: ignore[misc]
                if n_parameters == 3
                else DEFAULT_EDGE_WEIGHT
            )

            bidirectional = (
                cast(bool, entry[3])  # type: ignore[misc]
                if n_parameters == 4
                else True
            )

            graph.connect(
                source_node=source_node,
                target_node=target_node,
                weight=edge_weight,
                bidirectional=bidirectional,
            )
    return graph
