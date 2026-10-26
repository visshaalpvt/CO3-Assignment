# Median of Medians Algorithm

This folder documents the deterministic linear-time selection algorithm implemented in `Implementation_Code/advanced.py` (`median_of_medians_select`).

### Algorithm Concept:
- **Input**: Unsorted array $A$ of $n$ elements, rank index $k$ ($0 \le k < n$).
- **Grouping**: Partition $A$ into blocks of 5 elements.
- **Block Medians**: Sort each group in $O(1)$ and pick the median.
- **Pivot Selection**: Recursively find the median of the block medians.
- **Partitioning**: Partition array around the pivot into less than, equal to, and greater than sets.
- **Recurrence**:
  $$T(n) \le T(n/5) + T(7n/10) + O(n)$$
  Since $1/5 + 7/10 = 9/10 < 1$, the recurrence solves to $O(n)$ deterministic worst-case time.

See also: `Pseudocode/median_of_medians.txt`.
