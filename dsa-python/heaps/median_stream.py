import math
import heapq

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
    __max_heap: list[int]
    __min_heap: list[int]
    # __size: int

    def __init__(self) -> None:
        self.__max_heap = []
        self.__min_heap = []
        # self.__size = 0
        # raise NotImplementedError

    def add(self, num: int) -> None:
        max_heap_len = len(self.__max_heap)
        min_heap_len = len(self.__min_heap)

        if max_heap_len == 0:
            self.__max_heap.append(num)
            # self.__size += 1
            return

        if min_heap_len == 0:
            if num >= self.__max_heap[0]:
                self.__min_heap.append(num)
            else:
                prev_left_middle = heapq.heapreplace_max(self.__max_heap, num)
                self.__min_heap.append(prev_left_middle)
            # self.__size += 1
            return

        left_middle = self.__max_heap[0]

        if num < left_middle:
            if max_heap_len > min_heap_len:
                prev_left_middle = heapq.heappushpop_max(self.__max_heap, num)
                heapq.heappush(self.__min_heap, prev_left_middle)
            else:
                heapq.heappush_max(self.__max_heap, num)
        else:
            if min_heap_len > max_heap_len:
                prev_right_middle = heapq.heappushpop(self.__min_heap, num)
                heapq.heappush_max(self.__max_heap, prev_right_middle)
            else:
                heapq.heappush(self.__min_heap, num)
        # self.__size += 1
        return
        # raise NotImplementedError

    def median(self) -> float:
        left_side = self.__max_heap
        right_side = self.__min_heap

        median = 0.0
        if len(left_side) < len(right_side):
            median = right_side[0]
        elif len(right_side) < len(left_side):
            median = left_side[0]
        else:
            median = (left_side[0] + right_side[0]) / 2
        # print(median)
        return median

        # raise NotImplementedError


def _brute_median(seen: list[int]) -> float:
    # """Oracle helper. Sort + pick middle(s)."""
    # raise NotImplementedError
    seen.sort()
    size = len(seen)
    mid = math.floor(size / 2)
    median: float = 0.0
    if size % 2 == 1:
        median = seen[mid]
    else:
        median = (seen[mid] + seen[mid - 1]) / 2
    return median


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
