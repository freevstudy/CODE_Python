# 输入一个数，并指出该是否是10的整数倍

number = input("请输入一个整数：")
number = int(number)

if number % 10 == 0:
    print(f"数字{number}是10的整数倍。")
else:
    print(f"数字{number}不是10的整数倍。")
