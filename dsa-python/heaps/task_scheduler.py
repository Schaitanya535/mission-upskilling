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


def least_intervals(tasks: list[str], n: int) -> int:
    raise NotImplementedError


def brute_least_intervals(tasks: list[str], n: int) -> int:
    """Oracle. The closed-form formula — derive and use it to check the sim."""
    raise NotImplementedError


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
