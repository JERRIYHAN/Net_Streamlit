import streamlit as st
st.write("# P5 数据结构")

st.write("## 5-1")
st.code('''
answer=input("请输入句子:")
d={}
for i in answer:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if i not in d.keys():
            d[i]=1
        else:
            d[i]+=1
    if i in "abcdefghijklmnopqrstuvwxyz":
        if chr(ord(i)-32) not in d.keys():
            d[chr(ord(i)-32)]=1
        else:
            d[chr(ord(i)-32)]+=1
print(d)

''')

st.write("## 5-2")
st.code('''
data=input('请输入一组数，数间以空格间隔：')
data=data.split(' ')
data=list(map(int,data))
print(data)

''')

st.write("## 5-3")
st.code('''
i=0
d={}
while i != -1:
    ans=input("请输入:")
    if ans=="-1":
        break
    else:
        ans=ans.split(" ")
        d[ans[0]]=ans[1]


k=0
while k !=-1:
    z=input("查找：")
    if z == "xxx":
        break
    else:
        print(d.get(z,"无"))

''')

st.write("## 5-4")
st.code('''
alpha=[]
for i in range(65,65+26):
    alpha.append(chr(i))
num=[]
for k in range(1,27):
    num.append(k)
ziped=list(zip(alpha,num))
print(ziped)

''')

st.write("## 5-5")
st.code('''
num=[0,1,2,3,4,5,6,7,8,9]
alpha=["zero","one","two","three","four","five","six","seven","eight","nine"]

ziped=dict(zip(num,alpha))

ans=input("请输入：")
for i in ans:
    print(ziped.get(eval(i)), end=" ")

''')

st.write("## 5-6")
st.code('''
import random
original=[]
for i in range(10):
    original.append([])
    for j in range(5):
        original[i].append(random.randint(10,30))
print(original)

new=[]
for m in range(len(original[0])):
    new.append([])
    for n in range(len(original)):
        new[m].append(original[n][m])

print(new)

''')

st.write("## 5-7")
st.code('''
import random
original=[]
for i in range(10):
    original.append([])
    for j in range(5):
        original[i].append(random.randint(10,30))
print(original)

new=[[row[i] for row in original]
     for i in range(5)]

print(new)

''')