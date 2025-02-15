# 创建两个列表，空列表表示已经制作完成的三明治，每次制作完一个三明治就把制作完成的三明治移到空列表中，并打印一条消息说明。

sandwich_orders = ['火腿芝士', '烤鸡', '五香烟熏牛肉', '日式煎蛋', '三文鱼牛油果', '五香烟熏牛肉', '土耳其烤肉', '素食鹰嘴豆', '五香烟熏牛肉']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"我已经制作好了你需要的{current_sandwich}三明治。")
    finished_sandwiches.append(current_sandwich)

print("\n已经制作完成的三明治：")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich}三明治")

# 五香烟熏牛肉已经卖完了，需要打印消息指出来，并删掉列表中包含的五香烟熏牛肉。

print("\n五香烟熏牛肉卖完了。")

while '五香烟熏牛肉' in finished_sandwiches:
    finished_sandwiches.remove('五香烟熏牛肉')

print(finished_sandwiches)

