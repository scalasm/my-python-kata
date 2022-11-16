"""Unit tests for arrays merge."""
import pytest

from my_python_kata.algorithms.merge_arrays import merge_arrays


merge_arrays_test_data = [
    # A few arrays
    (
        [
            [1, 5, 7, 8],
            [0, 6, 8],
            [3, 7, 10],
        ],
        [0, 1, 3, 5, 6, 7, 7, 8, 8, 10],
    ),
    # Inlcude empty array
    (
        [
            [1, 5],
            [],
            [3, 4],
        ],
        [1, 3, 4, 5],
    ),
    # All empty arrays
    (
        [
            [],
            [],
        ],
        [],
    ),
    # Single array
    ([[1, 2, 3]], [1, 2, 3]),
]


@pytest.mark.parametrize("arrays,expected_result_array", merge_arrays_test_data)
def test_merge_arrays(
    arrays: list[list[int]], expected_result_array: list[int]
) -> None:
    """Test that merging works."""
    assert merge_arrays(arrays) == expected_result_array
