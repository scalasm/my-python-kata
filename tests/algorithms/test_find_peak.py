"""Unit tests for the find_peak module."""
from typing import cast
from typing import List
from typing import Optional

import pytest

from my_python_kata.algorithms.find_peak import find_peak_1d
from my_python_kata.algorithms.find_peak import find_peak_2d
from my_python_kata.algorithms.find_peak import Peak2D

find_peak_1d_test_data = [
    ([1, 2, 3, 0], 2, 3),
    ([1, 2], 1, 2),
    ([2, 1], 0, 2),
    ([1, 2, 3, 4], 3, 4),
    ([4, 3, 2, 1], 0, 4),
    ([1], 0, 1),
    ([], None, None),
]


@pytest.mark.parametrize(
    "array,expected_peak_position,expectected_peak_value", find_peak_1d_test_data
)
def test_find_peak_1d(
    array: List[int], expected_peak_position: int, expectected_peak_value: int
) -> None:
    """Test find_peak_1d() function."""
    peak_position: Optional[int] = find_peak_1d(array)

    assert peak_position == expected_peak_position

    if peak_position is not None:
        assert array[peak_position] == expectected_peak_value


find_peak_2d_test_data = [
    ([[1, 2, 3, 0], [2, 3, 2, 0], [1, 4, 7, 1], [1, 5, 3, 0]], Peak2D(2, 2), 7),
    ([[]], None, None),
    (
        [
            [1],
        ],
        Peak2D(0, 0),
        1,
    ),
    (
        [
            [1, 2, 3, 0],
        ],
        Peak2D(0, 2),
        3,
    ),
    ([[1], [2], [5], [1]], Peak2D(2, 0), 5),
    ([[1, 2, 1, 0], [2, 8, 2, 0], [1, 4, 2, 1], [1, 5, 1, 0]], Peak2D(1, 1), 8),
    ([[1, 2, 9, 0], [1, 2, 2, 0], [1, 1, 1, 1], [1, 1, 1, 0]], Peak2D(0, 2), 9),
]


@pytest.mark.parametrize(
    "array_2d,expected_peak_position,expectected_peak_value", find_peak_2d_test_data
)
def test_find_peak_2d(
    array_2d: List[List[int]],
    expected_peak_position: Peak2D,
    expectected_peak_value: int,
) -> None:
    """Test find_peak_2d() function."""
    peak_position: Optional[Peak2D] = find_peak_2d(array_2d)

    assert peak_position == expected_peak_position

    if peak_position is not None:
        row = cast(int, peak_position.row)
        column = cast(int, peak_position.column)

        assert array_2d[row][column] == expectected_peak_value


peak2d_test_data = [
    (Peak2D(2, 2), Peak2D(2, 2), True),
    (Peak2D(1, 0), Peak2D(2, 2), False),
    (Peak2D(1, 2), Peak2D(2, 2), False),
    (Peak2D(2, 1), Peak2D(2, 2), False),
    (None, Peak2D(2, 2), False),
    (Peak2D(None, None), Peak2D(2, 2), False),
    (Peak2D(None, None), Peak2D(None, None), True),
]


@pytest.mark.parametrize("first,second,expected_result", peak2d_test_data)
def test_peak2d_eq(first: Peak2D, second: Peak2D, expected_result: bool) -> None:
    """Test equality between Peak2D instances."""
    assert (first == second) == expected_result
