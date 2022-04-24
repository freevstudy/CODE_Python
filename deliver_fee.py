"""
输入行李的重量
20kg以内免费，超出20kg的部分，按照每kg1.5元收费

Date: 2022-04-24
"""

weight = float(input("请输入行李重量(kg)："))

if weight <= 20:
    print("这个行李的托运费免费。")
else:
    cost = (weight - 20) * 1.5
    print("这个行李的托运费为：%.2f元" %cost)
