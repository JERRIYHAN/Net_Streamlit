import streamlit as st

st.balloons()

st.logo("media/pythonimage.jpeg")
st.write("# P3合集 结构化程序设计")
st.write("## 3-1")
st.code('''
from math import *
a,b,c = eval(input("请输入a，b,c[用逗号分隔]"))
delta = b**2-4*a*c
if delta > 0:
    x1=(-b+sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-sqrt(b**2-4*a*c))/(2*a)
    print("x1为",x1,"x2为",x2)
elif delta == 0:
    x=-b/(2*a)
    print("x为",x)
else:
    print("无实根")
''')

st.write("## 3-2")
st.code('''
x = eval(input("请输入所花的钱"))
if x<1000:
    y=x
elif x<2000:
    y=0.9*x
elif x<3000:
    y=0.8*x
else:
    y=0.7*x
print("所付的钱",y,"元")

''')

st.write("## 3-3")
st.code('''
a=eval(input("请输入上网时间(h)："))
if a<10:
    sum=30
elif a<50:
    sum=30+2.5*(a-10)
else:
    sum=130+2*(a-50)

if sum>150:
    sum=150

print("上网费用为：",sum,"元")
''')

st.write("## 3-4")
st.code('''
x,y,z=eval(input("请输入x，y，z"))
list1=[x,y,z]
olist1=sorted(list1)
print(olist1[0],"<",olist1[1],"<",olist1[2])

''')

st.write("## 3-5")
st.code('''
m,n=eval(input("请输入总数和总腿数："))
if n%2!=0:
    print("腿数不为偶数，无法计算")
else:
    y=n/2-m
    x=m-y
    if m<0 or n<0 or x<0 or y<0:
        print("负数错误")
    else:
        if m!=int(m) or n!=int(n) or x!=int(x) or y!=int(y):
            print("小数错误")
        else:
            print(int(x),"只鸡",int(y),"只兔")
''')

st.write("## 3-6")
st.code('''
a=eval(input("请输入某门课的成绩："))
if a<0:
    print("逗我呢")
elif a<60:
    print("成绩为：",a,"绩点为：0")
elif a<70:
    print("成绩为：",a,"绩点为：2")
elif a<80:
    print("成绩为：",a,"绩点为：3")
elif a<90:
    print("成绩为：",a,"绩点为：4")
elif a<=100:
    print("成绩为：",a,"绩点为：5")
else:
    print("逗我呢")
''')

st.write("## 3-7")
st.code('''
import random
n=random.randint(5,11)
for z in range(n):
    print("\x20"*(n-z-1)+str(chr(97+z))*(2*z+1))
''')

st.write("## 3-8")
st.code('''
import random
n=random.randint(5,11)
if n%2==0:
    b=int(n/2)
    print(b)
    for z in range(b):
        print("\x20"*(b-z-1)+chr(65+z)*(2*z+1))
    for z in range(int(n/2),n):
        print("\x20"*(z-b)+chr(65+z)*(2*n-2*z-1))
else:
    c=n//2
    for z in range(c):
        print("\x20"*(c-z)+chr(65+z)*(2*z+1))
    print(chr(65+c)*n)
    for z in range(c+1,n):
        print("\x20"*(z-c)+chr(65+z)*(2*n-2*z-1))
''')

st.write("## 3-9")
st.code('''
iz=input("请输入表达式：")
suml=0
sumr=0
for a in z:
    if a=="(":
        suml+=1
    if a==")":
        sumr+=1
if suml==sumr:
    print("左括号等于右括号")
elif suml>sumr:
    print("左括号多于右括号")
else:
    print("左括号少于右括号")

''')

st.write("## 3-10")
st.code('''
a=input("请输入英文")
list1=a.split()
max1=0
q=len(list1)
for z in range(q):
    h=len(list1[z])
    if h > max1:
        max1=h
        z1=z
print(list1[z1])
print("其长度="+str(h))
        
''')

st.write("## 3-11")
st.code('''
a=eval(input("请输入正整数"))
z=1
while a>0:
    z=a%10
    print(z,end='')
    a=a//10
''')

st.write("## 3-12")
st.code('''
fenmu=1
s=0
n=1
while fenmu < 10000:
    s+=1/fenmu
    fenmu+=n
    n+=1
print(s)
''')

st.write("## 3-13")
st.code('''
import math
s=2
for i in range(1000):
    fenzi=(2*i+2)**2
    fenmu=(2*i+1)*(2*i+3)
    ji=fenzi/fenmu
    s=s*ji
print(s)
print(math.pi)
''')

st.write("## 3-14")
st.code('''
for i in range(100,1000):
    a=i//100
    b=i//10%10
    c=i%10
    if a**3+b**3+c**3==i:
        print(i)
''')

st.write("## 3-15")
st.code('''
a=eval(input("请输入a(1-9)"))
n=eval(input("请输入n(5-10)"))
temp=a
s=a
print("s="+str(a),end='')
for i in range(1,n):
    temp=temp*10+a
    print("+"+str(temp),end='')
    s+=temp
print("="+str(s))
''')

st.write("## 3-16")
st.code('''
for x in range(1,7):
    for y in range(x+1,7):
        for z in range(y+1,7):
            if z>=5:
                print("x于周%d考，y于周%s考，z于周%g考"%(x,y,z))
''')

st.write("## 3-17")
st.code('''
import random
a=random.randint(1,101)
k=0
n=0
while a!=k:
    k=eval(input("输入猜测的"))
    if a>k:
        print(k,"小了")
    if a<k:
        print(k,"大了")
    n+=1
print(k,"恭喜你","你猜了%d次"%(n))

''')





