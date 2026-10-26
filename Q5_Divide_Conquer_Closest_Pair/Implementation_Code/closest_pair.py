import math
def brute_force(points):
    best=float("inf"); pair=None; count=0
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            count+=1; d=math.dist(points[i],points[j])
            if d<best:best=d;pair=(points[i],points[j])
    return pair,best,count
def closest_pair(points):
    if len(points)<2: raise ValueError("at least two points required")
    px=sorted(points); py=sorted(points,key=lambda p:p[1]); count=[0]
    def rec(xset,yset):
        n=len(xset)
        if n<=3:
            pair,d,c=brute_force(xset); count[0]+=c; return pair,d
        mid=n//2; leftx=xset[:mid]; rightx=xset[mid:]; splitx=rightx[0][0]
        leftids=set(leftx); ly=[p for p in yset if p in leftids]; ry=[p for p in yset if p not in leftids]
        lp,ld=rec(leftx,ly); rp,rd=rec(rightx,ry)
        bestpair,best=(lp,ld) if ld<=rd else (rp,rd)
        strip=[p for p in yset if abs(p[0]-splitx)<best]
        for i in range(len(strip)):
            for j in range(i+1,min(i+8,len(strip))):
                count[0]+=1; d=math.dist(strip[i],strip[j])
                if d<best:best=d;bestpair=(strip[i],strip[j])
        return bestpair,best
    pair,d=rec(px,py)
    return pair,d,count[0]
if __name__=="__main__":
    pts=[(2,3),(12,30),(40,50),(5,1),(12,10),(3,4)]
    print("Brute force:",brute_force(pts))
    print("Divide and conquer:",closest_pair(pts))
