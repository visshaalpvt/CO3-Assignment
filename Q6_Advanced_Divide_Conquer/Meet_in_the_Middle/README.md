# Meet-in-the-Middle Algorithm

This folder documents the Meet-in-the-Middle subset sum algorithm implemented in `Implementation_Code/advanced.py` (`subset_sum_mitm`).

### Algorithm Concept:
- **Problem**: Given a set of $n$ integers and a target sum $S$, determine if a subset sums to $S$ and reconstruct the subset.
- **Brute Force**: Exhaustive search checks $2^n$ subsets ($O(2^n)$ time).
- **Meet-in-the-Middle Strategy**:
  1. Divide the array into two halves: $L$ of size $\lfloor n/2 \rfloor$ and $R$ of size $\lceil n/2 \rceil$.
  2. Generate all $2^{n/2}$ subset sums for each half.
  3. Sort the right half subset sums in $O(2^{n/2} \cdot n)$.
  4. For each sum $s \in L$, use binary search (`bisect_left`) to check if $S - s$ exists in $R$.
- **Time Complexity**: $O(2^{n/2} \cdot n)$ time and $O(2^{n/2})$ space, providing exponential speedup over naive $O(2^n)$.

See also: `Pseudocode/meet_in_middle.txt`.
