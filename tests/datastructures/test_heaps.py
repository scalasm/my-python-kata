"""Unit tests for the heap module."""

from typing import List

import pytest

from my_python_kata.datastructures.heaps import MaxHeap


max_heap_heapify_test_data = [
    ([3, 9, 2, 1, 4, 5], [9, 4, 5, 1, 3, 2]),
    ([3, 2, 1], [3, 2, 1]),  # Already sorted
    ([1, 2, 3], [3, 1, 2]),
    ([1, 2], [2, 1]),
    ([1], [1]),
    ([], []),
]


@pytest.mark.parametrize("data,expected_state", max_heap_heapify_test_data)
def test_max_heap_heapify(data: List[int], expected_state: List[int]) -> None:
    """Test construction of a new heap given an initial list of elements."""
    heap = MaxHeap[int](data)

    assert heap._data == expected_state


max_heap_insert_test_data = [
    ([], 1, [1]),
    ([1], 2, [2, 1]),
    ([2, 1], 3, [3, 1, 2]),
    ([3, 9, 2, 1, 4, 5], 1, [9, 4, 5, 1, 3, 2, 1]),
    ([3, 9, 2, 1, 4, 5], 7, [9, 4, 7, 1, 3, 2, 5]),
]


@pytest.mark.parametrize("data,new_item,expected_state", max_heap_insert_test_data)
def test_insert(data: List[int], new_item: int, expected_state: List[int]) -> None:
    """Test insertion (addition) of a new item to the heap."""
    heap = MaxHeap[int](data)

    heap.insert(new_item)

    assert heap._data == expected_state


max_heap_max_value_test_data = [
    ([], None),
    ([1], 1),
    ([2, 1], 2),
    ([3, 1, 2], 3),
    ([3, 9, 2, 1, 4, 5], 9),
]


@pytest.mark.parametrize("data,expected_max_item", max_heap_max_value_test_data)
def test_max(data: List[int], expected_max_item: int) -> None:
    """Test reading the max (top-most) element."""
    heap = MaxHeap[int](data)

    assert heap.max() == expected_max_item


max_heap_size_test_data = [
    ([], 0),
    ([1], 1),
    ([2, 1], 2),
    ([3, 1, 2], 3),
    ([3, 9, 2, 1, 4, 5], 6),
]


@pytest.mark.parametrize("data,expected_size", max_heap_size_test_data)
def test_size(data: List[int], expected_size: int) -> None:
    """Test heap size."""
    heap = MaxHeap[int](data)

    assert heap.size() == expected_size


max_heap_extract_test_data = [
    ([], None, None),
    ([1], 1, None),
    ([2, 1], 2, 1),
    ([3, 1, 2], 3, 2),
    ([3, 9, 2, 1, 4, 5], 9, 5),
]


@pytest.mark.parametrize(
    "data,expected_extracted_item,expected_next_max_item", max_heap_extract_test_data
)
def test_extract(
    data: List[int], expected_extracted_item: int, expected_next_max_item: int
) -> None:
    """Test removal of the max (top-most) element."""
    heap = MaxHeap[int](data)

    assert heap.extract() == expected_extracted_item
    assert heap.max() == expected_next_max_item


max_heap_remove_test_data = [
    ([], None, None, []),
    ([1], None, None, [1]),
    ([], 1, None, []),
    ([2, 1], 1, 1, [2]),
    ([2, 1], 2, 2, [1]),
    ([3, 1, 2], 1, 1, [3, 2]),
    ([3, 9, 2, 1, 4, 5], 4, 4, [9, 3, 5, 1, 2]),
]


@pytest.mark.parametrize(
    "data,item_to_remove,expected_removed_item,expected_state",
    max_heap_remove_test_data,
)
def test_remove(
    data: List[int],
    item_to_remove: int,
    expected_removed_item: int,
    expected_state: List[int],
) -> None:
    """Test removal of an arbitrary item from the heap."""
    heap = MaxHeap[int](data)

    assert heap.remove(item_to_remove) == expected_removed_item
    assert heap._data == expected_state
