import sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
sys.path.extend([str(R/"Q1_MaxMin_Binary_Search/Implementation_Code"),str(R/"Q2_MergeSort_QuickSort/Implementation_Code"),str(R/"Q3_Karatsuba_Multiplication/Implementation_Code"),str(R/"Q4_Strassen_Matrix_Multiplication/Implementation_Code"),str(R/"Q5_Divide_Conquer_Closest_Pair/Implementation_Code"),str(R/"Q6_Advanced_Divide_Conquer/Implementation_Code")])
from q1_algorithms import max_min,binary_search
from q2_sorting import merge_sort,quick_sort
from karatsuba import karatsuba
from strassen import strassen,conventional
from closest_pair import closest_pair,brute_force
from advanced import median_of_medians_select,quickselect,subset_sum_mitm
assert max_min([7,2,9,4,1,8,3,6])[:2]==(1,9)
assert binary_search([1,2,3,4,5],4)[0]==3 and binary_search([1,2,3],9)[0]==-1
assert merge_sort([3,1,2,1])==[1,1,2,3]
assert quick_sort([3,1,2,1])[0]==[1,1,2,3]
assert karatsuba(123456789,987654321)==123456789*987654321
A=[[1,7],[3,5]];B=[[1,3],[7,5]]
assert strassen(A,B,cutoff=1)==conventional(A,B)
pts=[(2,3),(12,30),(40,50),(5,1),(12,10),(3,4)]
assert abs(closest_pair(pts)[1]-brute_force(pts)[1])<1e-9
assert median_of_medians_select([7,2,9,4,1,8,3,6,5],4)==5
assert quickselect([7,2,9,4,1,8,3,6,5],4)==5
assert sum(subset_sum_mitm([3,4,7,9,11,13],17) or [])==17
print("PASS Q1 Max/Min and Binary Search")
print("PASS Q2 Merge Sort and Quick Sort")
print("PASS Q3 Karatsuba multiplication")
print("PASS Q4 Strassen matches conventional multiplication")
print("PASS Q5 closest pair matches brute force")
print("PASS Q6 Median of Medians, QuickSelect, Meet-in-the-Middle")
print("Q7 intentionally requires the missing Day-4 challenge prompt and genuine independent proposals.")
