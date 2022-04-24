"""
已知四边形长为a，宽为b，夹角为90度，判断四边形的形状

Date: 2022-04-24
"""

a = float(input("a = "))
b = float(input("b = "))

if 2 * a == 2 * b:
    print("这个四边形的形状是正方形。")
else:
    print("这个四边形的形状是长方形。")
