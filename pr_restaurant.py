class Restaurant:
    """模拟餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐馆的属性。"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """显示餐馆信息"""
        print(f"餐馆名称：{self.restaurant_name}")
        print(f"菜系类型：{self.cuisine_type}")

    def open_restaurant(self):
        """显示营业状态"""
        print(f"{self.restaurant_name}正在营业中！")


# 创建实例
restaurant = Restaurant("老北京烤鸭店", "中式正餐")

# 打印属性
print("餐馆名称属性：", restaurant.restaurant_name)
print("菜系类型属性：", restaurant.cuisine_type)

# 调用方法
print("\n餐馆详细信息：")
restaurant.describe_restaurant()

print("\n营业状态：")
restaurant.open_restaurant()

# 创建三个实例
restaurant1 = Restaurant("民族饭店", "西北菜")
restaurant2 = Restaurant("上海外婆家", "杭帮菜")
restaurant3 = Restaurant("麦当劳", "西式快餐")

# 调用三个实例的方法
print("\n餐馆详细信息：")
restaurant1.describe_restaurant()

print("\n餐馆详细信息：")
restaurant2.describe_restaurant()

print("\n餐馆详细信息：")
restaurant3.describe_restaurant()
