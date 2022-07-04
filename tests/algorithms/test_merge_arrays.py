"""Unit tests for arrays merge."""
from typing import List

import pytest

from my_python_kata.algorithms.merge_arrays import merge_arrays


merge_arrays_test_data = [
    (
        [
            [1, 5, 7, 8],
            [0, 6, 8],
            [3, 7, 10],
        ],
        [0, 1, 3, 5, 6, 7, 7, 8, 8, 10],
    ),
    (
        [
            [1, 5],
            [],
            [3, 4],
        ],
        [1, 3, 4, 5],
    ),
    (
        [
            [],
            [],
        ],
        [],
    ),
]


@pytest.mark.parametrize("arrays,expected_result_array", merge_arrays_test_data)
def test_merge_arrays(
    arrays: List[List[int]], expected_result_array: List[int]
) -> None:
    """Test that merging works."""
    assert merge_arrays(arrays) == expected_result_array
