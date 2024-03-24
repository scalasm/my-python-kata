"""Find peaks in unidimensional and bidimensional arrays."""

from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import cast


# Findind a peak in 1-dimensional and 2-dimensional arrays.
# For 1-dimensional arrays, complexity is O(lg2n)
# For 2-dimensional arrays, complexity is O(rows*lg2Columns)


def find_peak_1d(array: List[int]) -> Optional[int]:
    """Find any peak in the 1-dimensional array.

    By definition, an array "a" contains a peak only if, for a given element
    at position "i", we have that a[i] >= a[i-1] and a[i] >= a[i+1].
    """
    if not array:
        return None
    return _find_peak_1d(array, 0, len(array))


def _find_peak_1d(array: List[int], start: int, end: int) -> Optional[int]:

    middle: int = (start + end) // 2

    # left bigger than current, go left
    if middle > 0 and array[middle - 1] > array[middle]:
        return _find_peak_1d(array, start, middle - 1)

    if middle < len(array) - 1 and array[middle + 1] > array[middle]:
        return _find_peak_1d(array, middle + 1, end)

    return middle


@dataclass
class Peak2D:
    """Value object for containing the 2D coordinates of a peak."""

    row: Optional[int]
    column: Optional[int]


def find_peak_2d(array_2d: List[List[int]]) -> Optional[Peak2D]:
    """Find a peak in a bidimensional array.

    In a matrix, there is a peak if and only if, given an element (i,j),
    the elements respectively on top, bottom, left and right are all
    less or equal than (i,j).
    """
    if not array_2d or not array_2d[0]:
        return None

    return _find_peak_2d(array_2d, 0, len(array_2d))


def _find_peak_2d(
    array_2d: List[List[int]], start_row: int, end_row: int
) -> Optional[Peak2D]:
    middle_row: int = (start_row + end_row) // 2

    max_value_col: int = cast(int, find_peak_1d(array_2d[middle_row]))

    # left bigger than current, go left
    if (
        middle_row > 0
        and array_2d[middle_row - 1][max_value_col]
        > array_2d[middle_row][max_value_col]
    ):
        return _find_peak_2d(array_2d, start_row, middle_row - 1)

    if (
        middle_row < len(array_2d) - 1
        and array_2d[middle_row + 1][max_value_col]
        > array_2d[middle_row][max_value_col]
    ):
        return _find_peak_2d(array_2d, middle_row + 1, end_row)

    return Peak2D(middle_row, max_value_col)
