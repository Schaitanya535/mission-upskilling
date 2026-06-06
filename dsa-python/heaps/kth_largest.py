"""
Problem 1 — Kth largest element in an array.

Given nums and k, return the k-th LARGEST element (k-th in sorted-desc order,
not the k-th distinct).

    kth_largest([3,2,1,5,6,4], k=2) -> 5
    kth_largest([3,2,3,1,2,4,5,5,6], k=4) -> 4

Constraints: 1 <= k <= len(nums). Assume nums non-empty.

Brute force: sort desc, index [k-1]. State its Big-O before you start.

Heap insight to discover:
- You don't need the whole sorted order. You need a bar that holds the
  current top-k. What heap kind, and what lives at its root?
- This IS your M1 heap_search with text/score stripped away. Same shape.

Target complexity: O(n log k) time, O(k) space.
"""


def kth_largest(nums: list[int], k: int) -> int:
    raise NotImplementedError


def brute_kth_largest(nums: list[int], k: int) -> int:
    """Oracle. Sort-based. Write this first, test the heap version against it."""
    raise NotImplementedError


if __name__ == "__main__":
    cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
    ]
    for nums, k, want in cases:
        got = kth_largest(nums, k)
        assert got == want == brute_kth_largest(nums, k), (nums, k, got, want)
    print("ok")
