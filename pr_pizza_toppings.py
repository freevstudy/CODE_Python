# 提示用户输入一系列比萨配料，当输入'quit'时结束循环。

prompt = "\n请输入您需要的比萨配料："
prompt += "\n(当输入'quit'时会退出)"

toppings = ""
while toppings != "quit":
    toppings = input(prompt)

    if toppings != "quit":
        print(f"我们会将{toppings}添加到比萨中。")
