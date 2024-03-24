"""Heap data-structures."""

import logging
from typing import Generic
from typing import List
from typing import Optional
from typing import TypeVar
from typing import cast


# Generic data type per items in a data page
T = TypeVar("T")


class MaxHeap(Generic[T]):
    """A Max heap is a binary tree that enforce Max heap property.

    This means that the root element is always bigger that his children,
    for any given subtree.

    Insertion and extraction are performed in O(lg2 n).

    References:
    * https://www.programiz.com/dsa/heap-data-structure
    """

    _data: List[T] = []

    def __init__(self, data: List[T]) -> None:
        """Construct a new heap from the initial list of elements.

        Args:
            data: the list of initial elements for the heap.

        """
        self._data = data.copy()
        self._heapify(0)

    def insert(self, item: T) -> None:
        """Insert a new iterm in the heap.

        Args:
            item: the item to add
        """
        self._data.append(item)
        self._bubble_top(self.size() - 1)

    def max(self) -> Optional[T]:
        """Returns the current max item or None if the heap is empty."""
        return self._get_value_at(0)

    def extract(self) -> Optional[T]:
        """Returns the current max item and removes it from the heap.

        It will return None is the ehap is empty.
        """
        if self.size() == 0:
            return None

        root_value = self._remove_item_at_index(0)

        return root_value

    def remove(self, item: T) -> Optional[T]:
        """Removes the specified item from the heap.

        Note that this implementation will only remove the first occurrence
        and not deal with any duplicates.

        Args:
            item: the item to remove

        Returns:
            the removed item or None if no such item was found
        """
        if not item:
            return None

        if self.size() == 0:
            return None
        # O(n) in the array
        item_index = self._data.index(item)

        return self._remove_item_at_index(item_index)

    def _remove_item_at_index(self, item_index: int) -> Optional[T]:
        # swap the item to be removed with the last one, resize the array
        # and then heapify the sub-heap
        item = self._get_value_at(item_index)

        self._swap(item_index, self.size() - 1)

        self._data = self._data[:-1]

        self._heapify(item_index)

        return item

    def size(self) -> int:
        """Returns the number of items in this heap."""
        return len(self._data)

    def _heapify(self, this_node_index: int) -> None:
        this_node_value = self._get_value_at(this_node_index)
        if not this_node_value:
            return

        left_index = 2 * this_node_index + 1
        right_index = 2 * this_node_index + 2

        logging.info(f"_heapify({this_node_index}, {left_index}, {right_index}")

        left_value = self._get_value_at(left_index)
        right_value = self._get_value_at(right_index)

        if left_value:
            if this_node_value < left_value:  # type: ignore
                self._swap(this_node_index, left_index)
            self._heapify(left_index)

        if right_value:
            if this_node_value < right_value:  # type: ignore
                self._swap(this_node_index, right_index)
            self._heapify(right_index)

    def _bubble_top(self, i: int) -> None:
        # Already at root level, bail out
        if i == 0:
            return

        swapped = True
        while i > 0 and swapped:
            root_index = (i - 1) // 2
            root_value = cast(T, self._get_value_at(root_index))

            this_value = cast(T, self._get_value_at(i))

            if this_value > root_value:  # type: ignore
                self._swap(i, root_index)
                i = root_index
            else:
                # No need to examine other elements up to the root,
                # the heap condition is alread in place
                swapped = False

    def _swap(self, i: int, j: int) -> None:
        tmp = self._data[i]
        self._data[i] = self._data[j]
        self._data[j] = tmp

    def _get_value_at(self, i: int) -> Optional[T]:
        return self._data[i] if i >= 0 and i < self.size() else None
