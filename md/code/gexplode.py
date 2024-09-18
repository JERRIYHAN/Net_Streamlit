import math
import random

a = 0.2

for i in range(100):
    g = random.triangular(0.01,0.2)
    g = math.sqrt(a*g**2+(1-a)*g**2)
    print(g)
