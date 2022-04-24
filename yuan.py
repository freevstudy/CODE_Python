"""
求解一元二次方程

Date: 2022-04-24
"""
import math
from re import X

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
delta = b ** 2 - 4 * a * c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a
    print("此方程有两个不相等的解：")
    print("x1 = %.2f" %x1)
    print("x2 = %.2f" %x2)
elif delta == 0:
    x = -b / 2 * a
    print("此方程有一个解：%.2f" %x)
else:
    print("此方程无解。")
