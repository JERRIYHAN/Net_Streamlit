import math
theta=eval(input("请输入角度θ（度）："))
x=eval(input("请输入浮点数值 x："))
radian=math.pi/180*theta
fx=math.sin(radian)+math.log(math.fabs(x)+1)-math.sqrt(x**2+1)
print(fx)
