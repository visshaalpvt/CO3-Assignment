# CO3 Assignment — Divide-and-Conquer Algorithms (CSA06)

## 1. Course and Student Information

- **Course:** CSA06 — Design and Analysis of Algorithms
- **Assignment:** Assignment 3 – CO3 (Divide-and-Conquer Algorithms)
- **Deadline:** November 3 (as stated in the class announcement; note: verify LMS / faculty portal for authoritative marks breakdown)
- **Student A:** [Name: To be provided by student | Registration Number: To be provided by student]
- **Student B:** [Name: To be provided by student | Registration Number: To be provided by student]

---

## 2. Project Objectives

1. **Theoretical Understanding**: Implement and analyze classical and advanced divide-and-conquer paradigms, formulating exact recurrence relations and Master Theorem asymptotic bounds.
2. **Algorithmic Efficiency**: Demonstrate optimization techniques including comparison-count minimization (Max/Min), divide-and-combine arithmetic speedups (Karatsuba, Strassen), geometric boundary pruning (Closest Pair), and exponential search space reduction (Meet-in-the-Middle).
3. **Empirical Validation**: Validate implementations against mathematical ground truth and baseline brute-force solutions across multiple input scales ($n \in \{100, 500, 1000, 2000\}$).
4. **Collaborative Engineering Discipline**: Adhere to structured pair-programming standards where both students independently propose algorithmic solutions (Q7 Day-4 Challenge) before joint design integration and defense.

---

## 3. Overview of Questions (Q1 – Q7)

- **Q1: Max/Min & Binary Search**
  - *Max/Min*: Recursive array bisection reducing comparisons from $2n - 2$ (naive) to $\lceil 3n/2 \rceil - 2$.
  - *Binary Search*: Iterative logarithmic search on ordered arrays returning index and exact comparison counts.
- **Q2: Merge Sort & Quick Sort**
  - *Merge Sort*: Deterministic, stable divide-and-conquer sorting running in $O(n \log n)$ time.
  - *Quick Sort*: In-place sorting with randomized pivot selection, tracking comparison counts, recursion call stack depth, and partition balance ratios.
- **Q3: Karatsuba Large Integer Multiplication**
  - Sub-quadratic multiplication for arbitrarily large integers by decomposing numbers into high and low halves and using Gauss's trick ($z_1 = (a+b)(c+d) - z_2 - z_0$) to reduce four sub-multiplications to three.
- **Q4: Strassen Matrix Multiplication**
  - Sub-cubic matrix multiplication decomposing $n \times n$ matrices into blocks and computing 7 recursive matrix products. Includes automatic power-of-two padding and a configurable conventional crossover threshold.
- **Q5: Closest Pair of 2D Points**
  - Geometric divide-and-conquer finding the Euclidean closest pair in $O(n \log n)$ time by recursive vertical splitting and searching an $8$-point bounded vertical strip. Verified against brute-force $O(n^2)$.
- **Q6: Advanced Divide-and-Conquer**
  - *Median of Medians*: Deterministic linear-time $O(n)$ selection using groups of 5 to guarantee balanced pivots.
  - *Meet-in-the-Middle*: Subset sum optimization splitting an array of size $n$ into two halves of size $n/2$, reducing complexity from $O(2^n)$ to $O(n 2^{n/2})$ using binary search.
- **Q7: Day-4 Design Challenge**
  - Two-phase collaborative design framework containing independent proposals from Student A and Student B, a trade-off comparison matrix, and implementation templates ready for the faculty-issued problem statement.

---

## 4. Directory Structure

```text
CO3_Assignment/
├── .gitignore
├── README.md
├── Final_Report/
│   ├── CO3_Assignment_Report.pdf
│   └── Student_Contribution_Record_TEMPLATE.md
├── Q1_MaxMin_Binary_Search/
│   ├── Implementation_Code/
│   │   └── q1_algorithms.py
│   ├── Pseudocode/
│   │   ├── binary_search.txt
│   │   └── max_min.txt
│   └── Output_Screenshots/
│       └── README.md
├── Q2_MergeSort_QuickSort/
│   ├── Implementation_Code/
│   │   └── q2_sorting.py
│   ├── Pseudocode/
│   │   └── merge_quick_sort.txt
│   └── Output_Screenshots/
│       └── README.md
├── Q3_Karatsuba_Multiplication/
│   ├── Implementation_Code/
│   │   └── karatsuba.py
│   ├── Pseudocode/
│   │   └── karatsuba.txt
│   └── Output_Screenshots/
│       └── README.md
├── Q4_Strassen_Matrix_Multiplication/
│   ├── Implementation_Code/
│   │   └── strassen.py
│   ├── Pseudocode/
│   │   └── strassen.txt
│   └── Output_Screenshots/
│       └── README.md
├── Q5_Divide_Conquer_Closest_Pair/
│   ├── Implementation_Code/
│   │   └── closest_pair.py
│   ├── Pseudocode/
│   │   └── closest_pair.txt
│   └── Output_Screenshots/
│       └── README.md
├── Q6_Advanced_Divide_Conquer/
│   ├── Implementation_Code/
│   │   └── advanced.py
│   ├── Median_of_Medians/
│   │   └── README.md
│   ├── Meet_in_the_Middle/
│   │   └── README.md
│   ├── Pseudocode/
│   │   ├── median_of_medians.txt
│   │   └── meet_in_middle.txt
│   └── Output_Screenshots/
│       └── README.md
├── Q7_Day4_Design_Challenge/
│   ├── Implementation_Code/
│   │   └── README.txt
│   ├── Joint_Final_Design/
│   │   └── design_comparison_template.md
│   ├── Pseudocode/
│   │   └── final_design_pseudocode_template.txt
│   ├── Student_A_Initial_Design/
│   │   └── proposal_template.md
│   ├── Student_B_Initial_Design/
│   │   └── proposal_template.md
│   └── Output_Screenshots/
│       └── README.md
└── Supporting_Files/
    ├── ASSIGNMENT_SOURCE_NOTE.md
    ├── run_experiments.py
    ├── screenshots_README.txt
    ├── test_all.py
    ├── datasets/
    │   └── sample_data.json
    └── results/
        ├── experiment_results.csv
        ├── experiment_run_log.txt
        └── test_output.txt
```

---

## 5. Python Prerequisites

- **Python Version**: Python 3.8 or higher (tested with Python 3.11).
- **External Dependencies**: None. All implementations utilize the Python Standard Library (`math`, `random`, `time`, `sys`, `pathlib`, `csv`, `bisect`).
- **Operating System**: Platform-independent (compatible with Windows, Linux, and macOS).

---

## 6. Execution Instructions for Each Module

Execute from the root directory of the repository:

### Q1: Max/Min & Binary Search
```bash
python Q1_MaxMin_Binary_Search/Implementation_Code/q1_algorithms.py
```
*Expected Output:*
```text
MaxMin: (1, 9, 10)
Sorted data: [1, 2, 3, 4, 6, 7, 8, 9]
Search 6: (4, 3)
Search 5: (-1, 3)
```

### Q2: Merge Sort & Quick Sort
```bash
python Q2_MergeSort_QuickSort/Implementation_Code/q2_sorting.py
```
*Expected Output:*
```text
Merge: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Quick: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Quick stats: {'comparisons': 24, 'max_stack_depth': 6, 'partitions': [(9, 6, 2), (6, 5, 0), (5, 0, 4), (4, 0, 3), (3, 0, 2), (2, 1, 0), (2, 0, 1)]}
```

### Q3: Karatsuba Multiplication
```bash
python Q3_Karatsuba_Multiplication/Implementation_Code/karatsuba.py
```
*Expected Output:*
```text
Karatsuba: 1219326311370217952237463801111263526900
Correct: 1219326311370217952237463801111263526900 Match: True
```

### Q4: Strassen Matrix Multiplication
```bash
python Q4_Strassen_Matrix_Multiplication/Implementation_Code/strassen.py
```
*Expected Output:*
```text
Strassen: [[50, 38], [38, 34]]
Conventional: [[50, 38], [38, 34]]
```

### Q5: Closest Pair of Points
```bash
python Q5_Divide_Conquer_Closest_Pair/Implementation_Code/closest_pair.py
```
*Expected Output:*
```text
Brute force: (((2, 3), (3, 4)), 1.4142135623730951, 15)
Divide and conquer: (((2, 3), (3, 4)), 1.4142135623730951, 7)
```

### Q6: Advanced Divide-and-Conquer
```bash
python Q6_Advanced_Divide_Conquer/Implementation_Code/advanced.py
```
*Expected Output:*
```text
5th smallest (k=4): 5
Subset sum 17: [4, 13]
```

---

## 7. Test Harness Instructions

The unified test harness validates correctness across all implemented questions by asserting against mathematical invariants, baseline brute-force solutions, and built-in operations.

Run the test suite:
```bash
python Supporting_Files/test_all.py
```

*Expected Terminal Output:*
```text
PASS Q1 Max/Min and Binary Search
PASS Q2 Merge Sort and Quick Sort
PASS Q3 Karatsuba multiplication
PASS Q4 Strassen matches conventional multiplication
PASS Q5 closest pair matches brute force
PASS Q6 Median of Medians, QuickSelect, Meet-in-the-Middle
Q7 intentionally requires the missing Day-4 challenge prompt and genuine independent proposals.
```

---

## 8. Experiment Instructions

Empirical benchmarking evaluates running times and comparison counts across input sizes $n \in \{100, 500, 1000, 2000\}$:

```bash
python Supporting_Files/run_experiments.py
```

Results are printed to terminal and recorded to `Supporting_Files/results/experiment_results.csv`.

*Sample Recorded Measurements:*
| Algorithm | $n$ | Time (s) | Comparisons / Notes |
|:---|:---:|:---:|:---|
| `max_min` | 100 | $0.000067$ | 162 |
| `merge_sort` | 100 | $0.000355$ | Stable $O(n \log n)$ |
| `quick_sort_random_pivot` | 100 | $0.000283$ | 713 |
| `max_min` | 500 | $0.000251$ | 754 |
| `merge_sort` | 500 | $0.001179$ | Stable $O(n \log n)$ |
| `quick_sort_random_pivot` | 500 | $0.001533$ | 5,051 |
| `max_min` | 1000 | $0.000491$ | 1,510 |
| `merge_sort` | 1000 | $0.002575$ | Stable $O(n \log n)$ |
| `quick_sort_random_pivot` | 1000 | $0.004104$ | 11,385 |
| `max_min` | 2000 | $0.001017$ | 3,022 |
| `merge_sort` | 2000 | $0.006060$ | Stable $O(n \log n)$ |
| `quick_sort_random_pivot` | 2000 | $0.007606$ | 23,651 |

*Note: Runtime figures are machine-dependent. Students should run this script on their local machines to record hardware-specific execution times.*

---

## 9. Recurrence Relations and Complexity Summary

| Question / Algorithm | Recurrence Relation | Best Case | Average Case | Worst Case | Auxiliary Space |
|:---|:---|:---:|:---:|:---:|:---:|
| **Q1: Max-Min** | $T(n) = 2T(n/2) + 2$ | $\frac{3n}{2} - 2$ comps | $\frac{3n}{2} - 2$ comps | $\frac{3n}{2} - 2$ comps | $O(\log n)$ call stack |
| **Q1: Binary Search** | $T(n) = T(n/2) + O(1)$ | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(1)$ |
| **Q2: Merge Sort** | $T(n) = 2T(n/2) + \Theta(n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n \log n)$ | $\Theta(n)$ |
| **Q2: Quick Sort** | $T(n) = T(k) + T(n-k-1) + \Theta(n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ stack ($O(n)$ worst) |
| **Q3: Karatsuba** | $T(n) = 3T(n/2) + \Theta(n)$ | $\Theta(n^{\log_2 3}) \approx O(n^{1.585})$ | $O(n^{1.585})$ | $O(n^{1.585})$ | $O(n)$ |
| **Q4: Strassen Matrix** | $T(n) = 7T(n/2) + \Theta(n^2)$ | $\Theta(n^{\log_2 7}) \approx O(n^{2.807})$ | $O(n^{2.807})$ | $O(n^{2.807})$ | $O(n^2)$ |
| **Q5: Closest Pair** | $T(n) = 2T(n/2) + O(n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ |
| **Q6: Median of Medians** | $T(n) \le T(n/5) + T(7n/10) + O(n)$ | $O(n)$ | $O(n)$ | $O(n)$ | $O(n)$ |
| **Q6: Meet-in-the-Middle** | $T(n) = 2 \cdot 2^{n/2} + O(n 2^{n/2})$ | $O(n 2^{n/2})$ | $O(n 2^{n/2})$ | $O(n 2^{n/2})$ | $O(2^{n/2})$ |
| **Q7: Day-4 Challenge** | Dependent on final design | Pending | Pending | Pending | Pending |

---

## 10. Known Limitations and Missing Q7 Information

> [!IMPORTANT]
> **Academic Integrity Notice regarding Q7:**
> The provided assignment package outlines the two-phase collaboration methodology for the Day-4 Design Challenge but does not contain the faculty's specific challenge problem statement. In compliance with strict academic integrity standards:
> - No hypothetical problem has been substituted or claimed as faculty-assigned.
> - The Q7 proposal templates (`Student_A_Initial_Design`, `Student_B_Initial_Design`), comparison matrix (`Joint_Final_Design`), and pseudocode templates are preserved intact.
> - When the challenge is officially released, both students must independently complete their proposals prior to joint integration.

---

## 11. Contribution Record Instructions

In accordance with course guidelines, both students must understand all topics, cross-defend answers, and rotate primary ownership across questions.

1. Open `Final_Report/Student_Contribution_Record_TEMPLATE.md`.
2. Replace all placeholder fields with actual work performed by Student A and Student B for Q1 through Q7.
3. Detail specific primary contributions (e.g., recurrence proof, code implementation, test verification, profiling) and joint collaboration evidence.
4. Sign and date the completed record prior to submission.

---

## 12. Instructions for Capturing Genuine Execution Screenshots

To complete the submission dossier:
1. Run each script locally in your terminal.
2. Capture full terminal window screenshots showing the command line, execution output, and timestamps.
3. Save the screenshots in the designated directory for each question:
   - `Q1_MaxMin_Binary_Search/Output_Screenshots/`
   - `Q2_MergeSort_QuickSort/Output_Screenshots/`
   - `Q3_Karatsuba_Multiplication/Output_Screenshots/`
   - `Q4_Strassen_Matrix_Multiplication/Output_Screenshots/`
   - `Q5_Divide_Conquer_Closest_Pair/Output_Screenshots/`
   - `Q6_Advanced_Divide_Conquer/Output_Screenshots/`
   - `Q7_Day4_Design_Challenge/Output_Screenshots/` (after completing Q7)
4. Verify all screenshots are clearly legible before generating the final submission archive or report.
