import streamlit as st

st.write("# P8 数据可视化")
st.write("## 8-1")
st.code('''
import math
import matplotlib.pyplot as plt
import numpy as np
t=np.arange(0,2*math.pi,0.01)
cos=np.cos(t)
sin=np.sin(t)
x=2/3*200*(cos**3+sin)
y=2/3*200*(sin**3+cos)
plt.plot(x,y,'*')
plt.show()

''')
st.write("## 8-2")
st.code('''
import math
import numpy as np
import matplotlib.pyplot as plt
plt.title("Sin函数曲线")
plt.ylim(-1.2,1.2)
plt.xlim(-4,4)
plt.rcParams['font.sans-serif']=['Hiragino Sans GB']
plt.rcParams['axes.unicode_minus']=False
x=-math.pi
while x<=math.pi:
    sin=math.sin(x)
    plt.plot(x,sin,marker="*")
    x+=0.1
plt.plot([-4,4],[0,0],'#4fc3f7')
plt.plot([0,0],[-4,4],'#ff9800')
plt.text(0.1,-0.1,"0")
plt.text(-math.pi,-0.1,"-pi")
plt.text(math.pi,-0.1,"pi")
plt.text(3.8,-0.1,"X")
plt.text(0.1,1.1,"Y")
plt.show()

''')
st.write("## 8-3")
st.code('''
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
im=np.array(Image.open(r"/Users/jiaaijiajiazhangshi/Desktop/beixuan/ea689c79523fa7295e12d28dda32bfdb.jpg"))
hd=256*[0]
for i in range(im.shape[0]):
    for j in range(im.shape[1]):
        k=0.299*im[i,j,0]+0.587*im[i,j,1]+0.114*im[i,j,2]
        hd[int(k)]+=1
index=np.arange(0,257)
barwidth=0.5
plt.bar(index,hd,barwidth,alpha=1,color='k')
plt.show()

''')
st.write("## 8-4")
st.code('''
import math
import matplotlib.pyplot as plt
import numpy as np
plt.title("心形曲线-直角坐标系")
plt.rcParams['font.sans-serif'] = ['Hiragino Sans GB']
plt.rcParams['axes.unicode_minus']=False
plt.xlim(-1.5,1.5)
plt.ylim(-2.1,0.3)
a=1
theta=np.arange(0,2*math.pi,0.001)
rol=a*(1-np.sin(theta))
x=rol*np.cos(theta)
y=rol*np.sin(theta)
plt.plot(x,y,color='red')
plt.show()

''')
st.write("## 8-5")
st.code('''
import math
import numpy as np
import matplotlib.pyplot as plt
theta=np.arange(0,2*math.pi,0.01)
sin=np.sin(theta)
a=1
rol=a*(1-sin)
plt.polar(theta,rol)
plt.show()

''')
st.write("## 8-6")
st.code('''
import numpy
import math
import matplotlib.pyplot as plt
score = [0.16,0.28,0.32,0.14,0.05,0.05]
plt.rcParams['font.sans-serif']=['Hiragino Sans GB']
plt.title("各项消费支出")
labels = ['学习用品', '日常用品', '伙食费', '通讯费','娱乐费','其他开支']
plt.axis("equal")
plt.pie(score,labels=labels,autopct='%4.1f%%')
plt.legend(bbox_to_anchor=(0.9, 0.4))
plt.show()

''')
st.write("## 8-7")
st.code('''
import matplotlib.pyplot as plt
import numpy as np
import math
import jieba
fp1=open(r"/Users/jiaaijiajiazhangshi/Documents/CollegeFiles/Academic/CS_Python/三国演义数据文件/三国人名汇总utf8.txt","r")
fp2=open(r"/Users/jiaaijiajiazhangshi/Documents/CollegeFiles/Academic/CS_Python/三国演义数据文件/三国演义utf8.txt","r")
content=fp1.read()
actors=content.split()



wordslist=jieba.lcut(fp2.read())
ActorsNum={}
for actor in actors:
    if wordslist.count(actor)>100:
        ActorsNum[actor]=wordslist.count(actor)

items=list(ActorsNum.items())#把字典转换为列表，其中每个元素都为一个键值对
ac=len(items)

plt.rcParams['font.sans-serif']=['Hiragino Sans GB']
plt.bar(ActorsNum.keys(),ActorsNum.values(),width=0.4)

plt.show()
fp1.close()
fp2.close()

''特别注意！! .read()方法相当于在 ,"r" 的基础上把整个文件读成了一个字符串
    "r"方法反馈的结果是一个文件类型，需要close
    而.read()之后就是字符串，不需要close''

''')
st.write("## 8-8")
st.code('''
import matplotlib.pyplot as plt
import numpy as np
import math

fig1=plt.figure()
plt.subplots_adjust(hspace=0.6)#调节两个之间垂直距离
 

plt.rcParams['font.sans-serif']=['Hiragino Sans GB']
plt.rcParams['axes.unicode_minus']=False

fig1.add_subplot(211)
x1=np.linspace(-1,1,1000)
y1=x1**2
plt.xticks(np.arange(-1,1.25,0.25))
plt.yticks(np.arange(0,1.2,0.2))
plt.title("平方曲线")
plt.plot(x1,y1,color='b')

fig1.add_subplot(212)
x2=np.arange(0.1,0.92,0.02)
y2=1/x2
plt.xticks(np.arange(0.1,1,0.1))
plt.ylim(1,11)
plt.xlim(0.05,0.95)
plt.yticks(np.arange(2,12,2))
plt.title("倒数曲线")
plt.plot(x2,y2,color='g')

plt.show()

''')