from dataclasses import dataclass
from typing import List, Optional

# Findind a peak in 1-dimensional and 2-dimensional arrays.
# For 1-dimensional arrays, complexity is O(lg2n)
# For 2-dimnensional arrays, complexity is O(rows*lg2Columns)


def find_peak_1D(array: List[int]) -> Optional[int]:
    """
    Find any peak in the 1-dimensional array. By definition, an array "a" contains a peak only if, for a given
    element at position "i", we have that a[i] >= a[i-1] and a[i] >= a[i+1].
    """
    if not array:
        return None
    return _find_peak_1D(array, 0, len(array))


def _find_peak_1D(array: List[int], start: int, end: int) -> Optional[int]:

    middle: int = (start + end) // 2

    # left bigger than current, go left
    if middle > 0 and array[middle - 1] > array[middle]:
        return _find_peak_1D(array, start, middle - 1)

    if middle < len(array) - 1 and array[middle + 1] > array[middle]:
        return _find_peak_1D(array, middle + 1, end)

    return middle


@dataclass
class Peak2D:
    """Value object for containing the 2D coordinates of a peak"""

    row: int
    column: int


def find_peak_2D(array2D: List[List[int]]) -> Optional[Peak2D]:
    """
    In a matrix, there is a peak if and only if, given an element (i,j), the elements respectively on top, bottom,
    left and right are all lesser or equal than (i,j).
    """
    if not array2D or not array2D[0]:
        return None

    return _find_peak_2D(array2D, 0, len(array2D))


def _find_peak_2D(
    array2D: List[List[int]], startRow: int, endRow: int
) -> Optional[Peak2D]:
    middleRow: int = (startRow + endRow) // 2

    maxValueCol = find_peak_1D(array2D[middleRow])

    # left bigger than current, go left
    if (
        middleRow > 0
        and array2D[middleRow - 1][maxValueCol] > array2D[middleRow][maxValueCol]
    ):
        return _find_peak_2D(array2D, startRow, middleRow - 1)

    if (
        middleRow < len(array2D) - 1
        and array2D[middleRow + 1][maxValueCol] > array2D[middleRow][maxValueCol]
    ):
        return _find_peak_2D(array2D, middleRow + 1, endRow)

    return Peak2D(middleRow, maxValueCol)
