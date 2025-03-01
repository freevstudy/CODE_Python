def make_sandwiches(*ingredients):
    """概述要制作的三明治"""
    print("\n制作一个三明治需要添加的材料是：")
    for ingredient in ingredients:
        print(f"- {ingredient}")


make_sandwiches("白面包", "火腿片、切达奶脑、生菜、番茄片", "蛋黄酱")
make_sandwiches("英式松饼", "煎培根、煎蛋、生菜", "番茄酱")
make_sandwiches("全麦面包", "金枪鱼罐头、洋葱碎、黄瓜片", "美乃滋")
