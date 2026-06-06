"""
Problem 3 — Merge K sorted lists.

Given k already-sorted lists, merge into one sorted list.

    merge_k_sorted([[1,4,5],[1,3,4],[2,6]]) -> [1,1,2,3,4,4,5,6]
    merge_k_sorted([]) -> []
    merge_k_sorted([[]]) -> []

(Plain Python lists, not linked-list nodes — keep the focus on the heap.)

Brute force: concat all, sort. State its Big-O. Why does it throw away the
fact that each list is ALREADY sorted?

Heap insight to discover:
- At each step the next output is the smallest CURRENT head across the k
  lists. A heap of size k holding one candidate per list gives that in
  O(log k). Pop the min, then push the next element FROM THE SAME LIST.
- What do you store in the heap so you know which list to advance, and
  where you are in it? -> tuple (value, list_index, elem_index). Middle
  field also breaks ties so Python never compares two equal values further.
- This is the M8 sharded scatter-gather merge: each shard returns its
  sorted top-k, the coordinator k-way-merges them. Same algorithm.

Target: O(N log k), N = total elements.
"""


def merge_k_sorted(lists: list[list[int]]) -> list[int]:
    raise NotImplementedError


def brute_merge_k_sorted(lists: list[list[int]]) -> list[int]:
    """Oracle. Concat + sort."""
    raise NotImplementedError


if __name__ == "__main__":
    cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1], [0]], [0, 1]),
    ]
    for lists, want in cases:
        got = merge_k_sorted(lists)
        assert got == want == brute_merge_k_sorted(lists), (lists, got, want)
    print("ok")
