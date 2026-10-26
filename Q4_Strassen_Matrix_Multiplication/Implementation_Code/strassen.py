def conventional(A,B):
    n=len(A)
    if not n or len(B)!=n or any(len(r)!=n for r in A+B): raise ValueError("square equal-size matrices required")
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def add(A,B,sign=1): return [[A[i][j]+sign*B[i][j] for j in range(len(A))] for i in range(len(A))]
def split(A):
    n=len(A); h=n//2
    return [ [r[:h] for r in A[:h]], [r[h:] for r in A[:h]], [r[:h] for r in A[h:]], [r[h:] for r in A[h:]] ]
def join(a,b,c,d): return [a[i]+b[i] for i in range(len(a))]+[c[i]+d[i] for i in range(len(c))]
def strassen(A,B,cutoff=32):
    n=len(A)
    if not n or len(B)!=n or any(len(r)!=n for r in A+B): raise ValueError("square equal-size matrices required")
    size=1
    while size<n:size*=2
    X=[r[:]+[0]*(size-n) for r in A]+[[0]*size for _ in range(size-n)]
    Y=[r[:]+[0]*(size-n) for r in B]+[[0]*size for _ in range(size-n)]
    def rec(A,B):
        n=len(A)
        if n<=cutoff or n==1:return conventional(A,B)
        a,b,c,d=split(A); e,f,g,h=split(B)
        m1=rec(add(a,d),add(e,h)); m2=rec(add(c,d),e); m3=rec(a,add(f,h,-1))
        m4=rec(d,add(g,e,-1)); m5=rec(add(a,b),h); m6=rec(add(c,a,-1),add(e,f))
        m7=rec(add(b,d,-1),add(g,h))
        c11=add(add(add(m1,m4),m5,-1),m7)
        c12=add(m3,m5); c21=add(m2,m4); c22=add(add(add(m1,m3),m2,-1),m6)
        return join(c11,c12,c21,c22)
    C=rec(X,Y)
    return [r[:n] for r in C[:n]]
if __name__=="__main__":
    A=[[1,7],[3,5]]; B=[[1,3],[7,5]]
    print("Strassen:",strassen(A,B,cutoff=1))
    print("Conventional:",conventional(A,B))
