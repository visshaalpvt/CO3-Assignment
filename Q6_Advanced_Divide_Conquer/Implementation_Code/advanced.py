from bisect import bisect_left
def median_of_medians_select(a,k):
    if not 0<=k<len(a): raise IndexError("k out of range")
    a=list(a)
    def select(x,k):
        if len(x)<=5:return sorted(x)[k]
        groups=[sorted(x[i:i+5]) for i in range(0,len(x),5)]
        pivot=select([g[len(g)//2] for g in groups],len(groups)//2)
        lo=[v for v in x if v<pivot]; eq=[v for v in x if v==pivot]; hi=[v for v in x if v>pivot]
        if k<len(lo):return select(lo,k)
        if k<len(lo)+len(eq):return pivot
        return select(hi,k-len(lo)-len(eq))
    return select(a,k)
def quickselect(a,k):
    if not 0<=k<len(a): raise IndexError("k out of range")
    x=list(a)
    while True:
        p=x[len(x)//2]; lo=[v for v in x if v<p]; eq=[v for v in x if v==p]; hi=[v for v in x if v>p]
        if k<len(lo):x=lo
        elif k<len(lo)+len(eq):return p
        else:k-=len(lo)+len(eq);x=hi
def subset_sum_mitm(a,target):
    n=len(a); mid=n//2; L=a[:mid]; R=a[mid:]
    def sums(x):
        out=[]
        for mask in range(1<<len(x)):
            total=0; chosen=[]
            for i,v in enumerate(x):
                if mask>>i&1: total+=v; chosen.append(v)
            out.append((total,chosen))
        return out
    ls=sums(L); rs=sorted(sums(R),key=lambda z:z[0]); vals=[v for v,_ in rs]
    for s,chosen in ls:
        j=bisect_left(vals,target-s)
        if j<len(vals) and vals[j]==target-s:return chosen+rs[j][1]
    return None
if __name__=="__main__":
    data=[7,2,9,4,1,8,3,6,5]
    print("5th smallest (k=4):",median_of_medians_select(data,4))
    print("Subset sum 17:",subset_sum_mitm([3,4,7,9,11,13],17))
