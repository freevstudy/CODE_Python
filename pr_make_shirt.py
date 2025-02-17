# 制作一件T恤
def make_shirt(shirt_size, shirt_text = "拒绝焦虑"):
    """T恤的尺码和印刷字样"""
    print(f"你需要的T恤尺码是{shirt_size}号,需要在上面印的字样是‘{shirt_text}’。")

make_shirt("2X", "我爱中国" )   # 位置实参调用函数
make_shirt(shirt_text = "我爱我家", shirt_size = "M")   # 关键字调用函数
make_shirt("3X")    # 默认值调用

