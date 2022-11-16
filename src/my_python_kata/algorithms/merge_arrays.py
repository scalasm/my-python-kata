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

    n_first = len(first)
    n_second = len(second)

    while i < n_first and j < n_second:
        if first[i] <= second[j]:
            merged.append(first[i])
            i = i + 1
        else:
            merged.append(second[j])
            j = j + 1

    # Copy leftovers
    if i < n_first:
        merged += first[i:n_first]

    if j < n_second:
        merged += second[j:n_second]

    return merged
