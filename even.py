"""
判断一个数是否是偶数

Date: 2022-04-24
"""

num = int(input("请输入一个整数："))

if num % 2 == 0:
    print(str(num) + "是一个偶数。")
else:
    print(str(num) + "是一个奇数。")
