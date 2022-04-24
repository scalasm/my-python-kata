from typing import List


def merge_arrays(arrays: List[List[int]]) -> List[int]:
    """Given n sorted arrays as input, generate a single sorted array as output."""
    merged: List[int] = []
    for array in arrays:
        merged = _merge_two_arrays(merged, array)

    return merged


def _merge_two_arrays(first: List[int], second: List[int]) -> List[int]:
    i = 0  # index for first array
    j = 0  # index for second array
    merged: List[int] = []

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            merged.append(first[i])
            i = i + 1
        else:
            merged.append(second[j])
            j = j + 1

    # Copy leftovers
    while i < len(first):
        merged.append(first[i])
        i = i + 1

    while j < len(second):
        merged.append(second[j])
        j = j + 1

    return merged
