def karatsuba(x,y,cutoff_digits=18):
    if x<0 or y<0: return -karatsuba(abs(x),abs(y),cutoff_digits)*(1 if (x<0) != (y<0) else -1)
    if x==0 or y==0:return 0
    if min(len(str(x)),len(str(y)))<=cutoff_digits:return x*y
    m=max(len(str(x)),len(str(y)))//2; base=10**m
    a,b=divmod(x,base); c,d=divmod(y,base)
    z0=karatsuba(b,d,cutoff_digits); z2=karatsuba(a,c,cutoff_digits)
    z1=karatsuba(a+b,c+d,cutoff_digits)-z2-z0
    return z2*base*base+z1*base+z0

if __name__=="__main__":
    x=12345678901234567890; y=98765432109876543210
    print("Karatsuba:",karatsuba(x,y))
    print("Correct:",x*y, "Match:",karatsuba(x,y)==x*y)
