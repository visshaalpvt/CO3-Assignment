import sys, time, random, csv
from pathlib import Path
R=Path(__file__).resolve().parents[1]
sys.path.extend([str(R/"Q1_MaxMin_Binary_Search/Implementation_Code"),str(R/"Q2_MergeSort_QuickSort/Implementation_Code"),str(R/"Q5_Divide_Conquer_Closest_Pair/Implementation_Code")])
from q1_algorithms import max_min,binary_search
from q2_sorting import merge_sort,quick_sort
from closest_pair import closest_pair,brute_force
rng=random.Random(42); rows=[]
for n in [100,500,1000,2000]:
    a=[rng.randrange(0,10*n) for _ in range(n)]
    t=time.perf_counter(); mn,mx,c=max_min(a); dt=time.perf_counter()-t
    rows.append(["max_min",n,round(dt,6),c])
    t=time.perf_counter(); merge_sort(a); dt=time.perf_counter()-t
    rows.append(["merge_sort",n,round(dt,6),""])
    t=time.perf_counter(); _,stats=quick_sort(a); dt=time.perf_counter()-t
    rows.append(["quick_sort_random_pivot",n,round(dt,6),stats["comparisons"]])
out=R/"Supporting_Files/results/experiment_results.csv"
with out.open("w",newline="") as f:
    w=csv.writer(f); w.writerow(["algorithm","n","seconds","comparisons"]);w.writerows(rows)
print(out.read_text())
print("Times are environment-specific. Re-run locally for your own measurements.")
