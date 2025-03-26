import streamlit as st
st.write("# P4 函数与递归")

st.write("## 4-1")
st.code('''
def fibos(a):
    fblist=[1,1]
    for i in range(a):
        new=fblist[-1]+fblist[-2]
        fblist.append(new)
    return(fblist)
n=eval(input("请输入项"))
a=n-2
print(fibos(a))
        
''')

st.write("## 4-2")
st.code('''
def fun(m):
    n=2
    status=True
    while n<m:
        if m%n==0:
            status=False
            break
        n+=1
    return status
for i in range(2,101):
    if fun(i):
        print(i)
        
''')

st.write("## 4-3")
st.code('''
def fun(x):
    a=x//1000
    b=x//100-10*a
    c=x//10-100*a-10*b
    d=x%10
    ans=1000*d+100*c+10*b+a
    return(ans)
for i in range(1000,10000):
    if fun(i)==i:
        print(i)
        
''')

st.write("## 4-4")
st.code('''
import random
def Myfun(a,b=5):
    fail=0
    jige=0
    zhong=0
    liang=0
    you=0
    for i in range(len(a)):
        if a[i]<60:
            fail+=1
        elif a[i]<70:
            jige+=1
        elif a[i]<80:
            zhong+=1
        elif a[i]<90:
            liang+=1
        else:
            you+=1
    if b==5:
        return you
    elif b==4:
        return liang
    elif b==3:
        return zhong
    elif b==2:
        return jige
    elif b==1:
        return fail
a=[]
for z in range(1,31):
    n=random.randint(0,101)
    a.append(n)
ask=eval(input("请输入想查询的成绩"))
print(Myfun(a,3))
print(Myfun(a=a,b=3))
print(Myfun(a))
        
''')

st.write("## 4-5")
st.code('''
import math
def s(x):
    delta=1
    s=0
    n=1
    while delta>10**(-6):
        middle=(-1)**(n+1)*x**(2*n-1)/math.factorial(2*n-1)
        s+=middle
        n+=1
        delta=middle
    return s

x=eval(input(""))
print(s(x))
        
''')

st.write("## 4-6")
st.code('''
def sequation(n):
    x=0
    a=2*x**3-4*x**2+3*x-6
    mini=-10
    maxi=10
    for i in range(n):
        if a>0:
            maxi=x
            x=(mini+x)/2
            a=2*x**3-4*x**2+3*x-6
        if a<0:
            mini=x
            x=(maxi+x)/2
            a=2*x**3-4*x**2+3*x-6
    return x
print(sequation(5))
        
''')

st.write("## 4-7")
st.code('''
def shuixianhua():
    for i in range(100,1000):
       a=i//100
       b=i//10%10
       c=i%10
       if a**3+b**3+c**3==i:
         print(i)

shuixianhua()
        
''')

st.write("## 4-8")
st.code('''
def f(n):
    fblist=[0,1]
    for i in range(n):
        new=fblist[-1]+fblist[-2]
        fblist.append(new)
    return(new)
n=eval(input("请输入项"))
a=n-2
if n==1:
    print("0")
elif n==2:
    print("1")
else:
    print(f(a))
        
''')

st.write("## 4-9")
st.code('''
def Trans(d,r):
    shang=1
    strnum=""
    while shang!=0:
        shang=d//r
        yu=d%r
        d=shang
        strnum+=str(yu)
    for i in range(-1,-len(strnum)-1,-1):
        print(strnum[i],end="")
d,r=eval(input(""))
Trans(d,r)
        
''')

st.write("## 4-10")
st.code('''
def reverse1(a):
    reL=[]
    z=-len(a)-1
    for i in range(-1,z,-1):
        reL.append(a[i])
    return reL


print(reverse1([1,2,3]))
        
''')

