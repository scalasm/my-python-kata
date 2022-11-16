"""Module that exposes how to merge two lists into one single list."""


def merge_arrays(arrays: list[list[int]]) -> list[int]:
    """Given n sorted arrays as input, generate a single sorted array as output."""
    if not arrays:
        return []

    if len(arrays) == 1:
        return arrays[0]

    merged: list[int] = arrays[0].copy()
    for i in range(1, len(arrays)):
        merged = _merge_two_arrays(merged, arrays[i])

    return merged


def _merge_two_arrays(first: list[int], second: list[int]) -> list[int]:
    i = 0  # index for first array
    j = 0  # index for second array
    merged: list[int] = []

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
