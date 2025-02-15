# 编写一个调查用户梦想的度假胜地的程序。
responses = {}

polling_active = True

while polling_active:
    name = input("\n请输入您的姓名：")
    response = input("请输入您梦想的度假胜地：")

    responses[name] = response

    repeat = input("还需要继续输入其他人的信息吗？（是 / 否)")
    if repeat == '否':
        polling_active = False

print("\n---调查结果---")
for name, response in responses.items():
    print(f"{name}梦想的度假胜地是{response}。")

