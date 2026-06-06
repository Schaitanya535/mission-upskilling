"""
Problem 4 — Find median from a data stream.

Numbers arrive one at a time. After each, you may be asked the median of all
seen so far. Median = middle (odd count) or mean of two middles (even count).

    mf = MedianFinder()
    mf.add(1); mf.add(2)
    mf.median()        # 1.5
    mf.add(3)
    mf.median()        # 2.0

Brute force: keep a list, sort on every median() call. State its Big-O per
query. Why is re-sorting each query wasteful?

Heap insight to discover (the classic two-heap trick):
- Split the data into a LOW half and a HIGH half.
- Low half -> MAX-heap (its largest is the boundary, easy to peek).
- High half -> MIN-heap (its smallest is the boundary).
- Keep sizes balanced (differ by at most 1). The median is then either the
  top of the bigger heap, or the average of both tops.
- On add(): push to one side, then rebalance by moving one element across.
  Work out the push-which-side + rebalance rule so the invariant always holds.
- Python max-heap: negate values going into the low heap.

Target: O(log n) add, O(1) median.
"""


class MedianFinder:
    def __init__(self) -> None:
        raise NotImplementedError

    def add(self, num: int) -> None:
        raise NotImplementedError

    def median(self) -> float:
        raise NotImplementedError


def _brute_median(seen: list[int]) -> float:
    """Oracle helper. Sort + pick middle(s)."""
    raise NotImplementedError


if __name__ == "__main__":
    import random

    mf = MedianFinder()
    seen: list[int] = []
    for _ in range(200):
        x = random.randint(-50, 50)
        mf.add(x)
        seen.append(x)
        assert mf.median() == _brute_median(seen), (seen, mf.median())
    print("ok")
