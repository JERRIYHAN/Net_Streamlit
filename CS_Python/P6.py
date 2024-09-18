import streamlit as st

st.write("# P6 数据文件")
st.write("## 6-1")
st.code('''
fp = open(r"/Users/jiaaijiajiazhangshi/Documents/CollegeFiles/Academic/CS_Python/Scores_u8.txt", mode='r', encoding='utf-8')
m=[]
while True:
    stra=fp.readline()
    if not stra:
        break
    c=eval(stra.split()[2])
    m.append(c)
print(m)
avg=sum(m)/len(m)
print("平均分为%d"%(avg))
print("最高分为%d"%(max(m)))
print("最低分为%d"%(min(m)))
fp.close()

''')

st.write("## 6-2")
st.code('''
fp1=open(r"/Users/jiaaijiajiazhangshi/Documents/CollegeFiles/Academic/CS_Python/T1.txt","r")
fp2=open(r"/Users/jiaaijiajiazhangshi/Documents/CollegeFiles/Academic/CS_Python/T2.txt","w")
n=0
new=""
fp2.seek(0)
while True:
    z=fp1.readline()
    if not z:
        break
    n+=1
    #print(z)
    for i in z:
        if i in "abcdefghijklmnopqrstuvwxyz":
            i_re=chr(ord(i)-32)
            new+=i_re
        elif i in "QWERTYUIOPASDFGHJKLZXCVBNM":
            i_re=chr(ord(i)+32)
            new+=i_re
        else:
            new+=i

    #print(new)
    fp2.write(new)
    new=""
            
    
print("文件共有%d行"%(n))
fp1.close()
fp2.close()

''')

st.write("## 6-3")
st.code('''
fp1 = open(r"/Users/jiaaijiajiazhangshi/Documents/CollegeFiles/Academic/CS_Python/JJ.txt","r")
fp2 = open(r"/Users/jiaaijiajiazhangshi/Documents/CollegeFiles/Academic/CS_Python/NewJJ.txt","w")

list_name=[]
list_num=[]
list_index=[]
d={}

while True:
    z=fp1.readline()
    if not z:
        break
    #print(z,end="")
    zz=z.split(",")
    #print(zz)
    number=zz[2][:-2]
    if number != '':
        numb=eval(number)
        list_index.append(zz[0])
        list_name.append(zz[1])
        list_num.append(numb)
d=list(zip(list_num,list_name,list_index))
    
#print(list_name)
print(list_num)


d.sort(key=lambda b:b[0],reverse=False)
print(d)
#print(list_num)

for i in d:
    fp2.write(i[2]+",")
    fp2.write(i[1]+",")
    fp2.write("%.2f元"%(i[0])+"\n")

#print(dd)
fp1.close()
fp2.close()

''')

st.write("## 6-4")
st.code('''
import jieba
fp=open(r"/Users/jiaaijiajiazhangshi/Documents/CollegeFiles/Academic/CS_Python/第七十回.txt").read()
wordslist=jieba.lcut(fp)
actors=[('贾宝玉','宝玉'),("林黛玉","黛玉")]
ActorsNum={}
for actor in actors:
    ActorsNum[actor[0]]=wordslist.count(actor[0])+wordslist.count(actor[1])
items=list(ActorsNum.items()) #转换成列表之后方可排序
items.sort(key=lambda x:x[1],reverse=True)
#print(items)
for i in items:
    print(i[0],end=" ")
    print(i[1])

''')

st.write("## 6-5")
st.code('''
from PIL import Image
im = Image.open(r"/Users/jiaaijiajiazhangshi/Documents/CollegeFiles/Academic/CS_Python/IMG_3450.png")
im = im.convert("L")
im = im.point(lambda x:255 if x>127 else 0)
im.save(r"/Users/jiaaijiajiazhangshi/Documents/CollegeFiles/Academic/CS_Python/IMG_3450_co.png")
im.show()

''')

st.write("## 6-6")
st.code('''
from PIL import Image
im = Image.open(r"/Users/jiaaijiajiazhangshi/Documents/CollegeFiles/Academic/CS_Python/XP.jpg")
im = im.convert("L")
im.show()
im = im.point(lambda x:255 if x>110 else 0)
im.save(r"/Users/jiaaijiajiazhangshi/Documents/CollegeFiles/Academic/CS_Python/New_XP.jpg")
im.show()

''')

st.write("## 6-7")
st.code('''
from PIL import Image
im = Image.open(r"/Users/jiaaijiajiazhangshi/Documents/CollegeFiles/Academic/CS_Python/XP.jpg")

print(im.size)
print(im.mode)
print(im.format)

''')

st.write("## 6-8")
st.code('''
from PIL import Image
im = Image.open(r"/Users/jiaaijiajiazhangshi/Documents/CollegeFiles/Academic/CS_Python/XP.jpg")
im.thumbnail((128,72))
im.show()
im.save(r"/Users/jiaaijiajiazhangshi/Documents/CollegeFiles/Academic/CS_Python/New_XP.jpg")

#img2=im.thumbnail((128,72))
#print(type(img2))
#img2.show()

''')

st.write("## 6-9")
st.code('''
from PIL import Image
from PIL import ImageEnhance
im = Image.open(r"/Users/jiaaijiajiazhangshi/Documents/CollegeFiles/Academic/CS_Python/XP.jpg")

thumbnail_size = (128,72)
im.thumbnail(thumbnail_size)
im.save(r"/Users/jiaaijiajiazhangshi/Documents/CollegeFiles/Academic/CS_Python/New_XP.jpg")

''')

st.write("## 6-15To17")
st.code('''
import jieba
list1=jieba.lcut('我来到上海同济大学',cut_all=True)
print(list1)

''')

st.write("## 6-18")
st.code('''
import jieba
fp=open(r"/Users/jiaaijiajiazhangshi/Documents/CollegeFiles/Academic/CS_Python/Tj.txt").read()

for ch in '，、。！;“”':
        fp = fp.replace(ch," ")

print(fp)
excludes={' ',"\n"}

words=jieba.lcut(fp)

counts = {}
for word in words:           
    #counts[word] = counts.get(word,0) + 1
    c = words.count(word)      
    counts[word] = c

for word in  excludes:
    del(counts[word]) #删除字典里的键，键值对就删掉了

items = list(counts.items()) #转为列表方可排序
items.sort(key=lambda x:x[1], reverse=True)

for i in range(3):
    word, count = items[i]
    print ("%s,%s"%(word,count))

''')


    
