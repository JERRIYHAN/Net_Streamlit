a,b=eval(input("qingshuru"))
def gcd(m,n):
    if m>n:
        if m%n==0:
            return n
        else:
            p=m%n
            return gcd(n,p)
    else:
        if n%m==0:
            return m
        else:
            p=n%m
            return gcd(m,p)
print(gcd(a,b))
        
