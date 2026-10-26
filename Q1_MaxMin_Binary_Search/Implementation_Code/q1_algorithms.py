def max_min(a):
    if not a: raise ValueError("input must not be empty")
    comparisons = 0
    def rec(lo, hi):
        nonlocal comparisons
        if lo == hi: return a[lo], a[lo]
        if hi == lo + 1:
            comparisons += 1
            return (a[lo], a[hi]) if a[lo] <= a[hi] else (a[hi], a[lo])
        mid = (lo + hi)//2
        mn1, mx1 = rec(lo, mid); mn2, mx2 = rec(mid+1, hi)
        comparisons += 2
        return min(mn1,mn2), max(mx1,mx2)
    mn,mx=rec(0,len(a)-1)
    return mn,mx,comparisons

def binary_search(a, target):
    low, high, comparisons = 0, len(a)-1, 0
    while low <= high:
        mid = low + (high-low)//2
        comparisons += 1
        if a[mid] == target: return mid, comparisons
        if a[mid] < target: low = mid+1
        else: high = mid-1
    return -1, comparisons

if __name__ == "__main__":
    values=[7,2,9,4,1,8,3,6]
    print("MaxMin:", max_min(values))
    ordered=sorted(values)
    print("Sorted data:", ordered)
    print("Search 6:", binary_search(ordered,6))
    print("Search 5:", binary_search(ordered,5))
