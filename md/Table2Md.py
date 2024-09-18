import sys
print("Enter a multi-lines: ")
lines = sys.stdin.read()        # 读取到文件尾

z=lines.split("\n")
# z是以行为单位的列表

for i in range(len(z)):
    temp=z[i] # temp是每行的元素

    a=temp.split('\t')
     # a是以单词为元素的列表


    new='|'
    for j in range(len(a)):
        if "|" in a[j]:
            b=list(a[j])
            
            lindex=[]
            for k in range(len(b)):
                if b[k]=="|":
                    lindex.append(k)
            #print(lindex)
            #lindex是“｜”符号的位置的集合列表
            n=0
            for m in range(len(lindex)):
                b.insert(lindex[m]+n,'\\')
                n+=1
            
            c="".join(b)
            new+=c
            new+="|"
            
        else:
            new+=a[j]
            new+="|"
    if i==1:
        print("|:-:|:-:|:-:|")
        print(new)
    else:
        print(new)
