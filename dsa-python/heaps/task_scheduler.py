import heapq

"""
Problem 5 (stretch) — Task scheduler.

Tasks are labelled by letter. Identical tasks must be separated by a cooldown
of n intervals. Each interval runs one task or sits idle. Return the MINIMUM
intervals to finish all tasks.

    least_intervals(["A","A","A","B","B","B"], n=2) -> 8
        # A B idle A B idle A B
    least_intervals(["A","A","A","B","B","B"], n=0) -> 6
    least_intervals(["A","A","A","A","B","C","D","E"], n=2) -> ?

Brute force / simulation: each interval, pick any runnable task. Greedy choice
matters — picking wrong idles more. State why naive picking fails.

Heap insight to discover:
- Greedy: at each step run the task with the MOST remaining count that is
  off cooldown -> max-heap on remaining count.
- Cooldown means a popped task can't go straight back. Hold it aside for n
  intervals (a queue of (ready_time, count)) then return it to the heap.
- There's also a closed-form: driven by the most frequent task and how many
  share that max frequency. Derive it, then check it against your heap sim.

Target: O(total_tasks) with the heap+queue simulation.
"""


def get_freq(tasks: list[str]) -> dict[str, int]:
    freq: dict[str, int] = {}
    for task in tasks:
        freq[task] = freq.get(task, 0) + 1
    return freq


def least_intervals(tasks: list[str], n: int) -> int:
    """
    Idea is that on every iteration, we will first look at the cooldown heap
    if the items on the cooldown heap are cooled, we will move back to the
    processing heap.

    Process them (print and reduce the count) and put them in the heap. At
    any point of time if the processing heap is empty but the cooldown heap
    isn't then we will print idle.

    We will end the program when both the heaps are empty
    """

    process_heap = [(freq, task) for (task, freq) in get_freq(tasks).items()]
    heapq.heapify_max(process_heap)
    # cool down q will be a (min) heap with the shape of tuple(cooldown_tick, frequency, task_name) .
    cool_down_q: list[tuple[int, int, str]] = []

    tick = 0
    while len(cool_down_q) != 0 or len(process_heap) != 0:
        while (cool_down_q) and (cool_down_q[0][0] < tick):
            top = heapq.heappop(cool_down_q)
            heapq.heappush_max(process_heap, (top[1], top[2]))

        if len(process_heap) == 0:
            # idle case
            tick += 1
            continue
        top = heapq.heappop_max(process_heap)
        if top[0] - 1 > 0:
            # reduce the count and put it in the cooldown q
            heapq.heappush(cool_down_q, (tick + n, top[0] - 1, top[1]))
        tick += 1
    return tick


def brute_least_intervals(tasks: list[str], n: int) -> int:
    """
    Build the skeleton from the most frequent task.
    Let maxf = highest count, cnt_max = how many tasks tie at maxf.

    Place the max-freq task with mandatory gaps:
    A . . A . . A          maxf=3, n=2
    - (maxf - 1) gaps between the A's.
    - Each gap is width (n + 1) (the A itself + n cooldown slots).
    - That's (maxf - 1) * (n + 1) cells for the first maxf-1 rows.
    - Final row: the last A, plus one slot for each other task that also
    hit maxf → add cnt_max.

    (maxf - 1) * (n + 1) + cnt_max

    The catch — too many distinct tasks fill the gaps. If you have so many
    tasks they spill past the skeleton, there are zero idles and the answer
    is just len(tasks). Formula can undercount there. So:
    return max(formula, len(tasks))
    """

    freq = get_freq(tasks)
    max_freq = max(freq.values())
    cnt_max = sum(1 for val in freq.values() if val == max_freq)
    formula = (max_freq - 1) * (n + 1) + cnt_max
    return max((formula), len(tasks))


if __name__ == "__main__":
    cases = [
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "A", "A", "B", "B", "B"], 0, 6),
        (["A", "B", "C", "D"], 2, 4),
    ]
    for tasks, n, want in cases:
        got = least_intervals(tasks, n)
        assert got == want == brute_least_intervals(tasks, n), (tasks, n, got, want)
    print("ok")
