result=""
def convert(d,r):
    global result
    z=d%r
    s=d//r
    if s==0:
        n=result+str(z)
        n=n[::-1]
        return n
    else:
        result+=str(z)
        return convert(s,r)
d,r=eval(input("qingshuru"))
print(convert(d,r))
    
    
