import random
def merge_sort(a):
    if len(a)<=1: return list(a)
    m=len(a)//2
    l,r=merge_sort(a[:m]),merge_sort(a[m:])
    out=[]; i=j=0
    while i<len(l) and j<len(r):
        if l[i]<=r[j]: out.append(l[i]); i+=1
        else: out.append(r[j]); j+=1
    return out+l[i:]+r[j:]

def quick_sort(a, seed=1):
    a=list(a); rng=random.Random(seed); stats={"comparisons":0,"max_stack_depth":0,"partitions":[]}
    def partition(lo,hi):
        p=rng.randrange(lo,hi+1); a[p],a[hi]=a[hi],a[p]; pivot=a[hi]; i=lo
        for j in range(lo,hi):
            stats["comparisons"]+=1
            if a[j]<=pivot: a[i],a[j]=a[j],a[i]; i+=1
        a[i],a[hi]=a[hi],a[i]
        stats["partitions"].append((hi-lo+1,i-lo,hi-i))
        return i
    def sort(lo,hi,depth=1):
        if lo>=hi:return
        stats["max_stack_depth"]=max(stats["max_stack_depth"],depth)
        p=partition(lo,hi); sort(lo,p-1,depth+1); sort(p+1,hi,depth+1)
    sort(0,len(a)-1)
    return a,stats

if __name__=="__main__":
    data=[9,1,7,3,8,2,6,4,5]
    print("Merge:",merge_sort(data))
    print("Quick:",quick_sort(data)[0])
    print("Quick stats:",quick_sort(data)[1])
