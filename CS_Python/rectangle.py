length=eval(input("输入矩形的长："))
if length<0 or length==0:
    print("长度不合理")
else:
    width=eval(input("输入矩形的宽："))
    if width<0 or width==0:
        print("宽度不合理")
    else:
        if length==width:
            print("这是正方形")
        else:
            print("这是长方形")
        s=width*length
        c=2*(width+length)
        print("矩形的面积为:",s)
        print("矩形的周长为:",c)
