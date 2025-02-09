# 询问客户有多少人用餐，如果超过8人，就指出没有空桌，否则指出有空桌。

prompt = "欢迎光临XX餐馆！"
prompt += "\n请问您有多少人来用餐？"

number = input(prompt)
number = int(number)

if number > 8:
    print("\n您预定人数已经超过8人，没有多余的空桌。")
else:
    print("\n您预定的人数未超过8人，欢迎前来用餐。")
