# 根据输入的年龄收取不同电影票价

active = True

while active:
    age_input = input("请输入您的年龄（输入quit时退出）：")
    if age_input == "quit":
        active = False
        break

    age = int(age_input)

    if age < 3:
        print("您可以免费观看电影。")
    elif 3 <= age <= 12:
        print("您的票价为10美元。")
    else:
        print("您的票价为15美元。")
