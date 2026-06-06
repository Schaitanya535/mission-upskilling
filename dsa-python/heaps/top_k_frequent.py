"""
Problem 2 — Top K frequent elements.

Given nums and k, return the k most frequent elements (any order).

    top_k_frequent([1,1,1,2,2,3], k=2) -> [1,2]
    top_k_frequent([1], k=1) -> [1]

Constraints: k is in range [1, number of distinct elements].

Brute force: count, sort items by count desc, take k. State its Big-O.

Heap insight to discover:
- Two stages: (1) build counts, (2) pick top-k BY count. Stage 2 is
  problem 1 again, but the heap key is the count, payload is the element.
- Tuple ordering: push (count, element). Why does element being comparable
  here save you from the tie-break footgun you'd hit with richer payloads?
- Bonus: O(n) bucket-sort alternative (index buckets by frequency). When
  does that beat the heap?

Target: O(n log k).
"""


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    raise NotImplementedError


def brute_top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Oracle. Count + sort."""
    raise NotImplementedError


if __name__ == "__main__":
    cases = [
        ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
        ([1], 1, {1}),
        ([4, 4, 4, 6, 6, 7, 7, 7, 7], 2, {4, 7}),
    ]
    for nums, k, want in cases:
        got = set(top_k_frequent(nums, k))
        assert got == want, (nums, k, got, want)
        assert set(brute_top_k_frequent(nums, k)) == want
    print("ok")
