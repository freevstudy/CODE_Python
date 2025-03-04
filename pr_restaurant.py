"""
创建一个名为Restaurant的类，为其方法__init__()设置属性restaurant_name和cuisine_type。
创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。
添加一个名为number_served的属性，并将其默认值设置为0。根据这个类创建一个名为restaurant的实例。打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
添加一个名为set_number_served()的方法，让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
添加一个名为increment_number_served()的方法，让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
"""

class Restaurant:
	"""模拟一个餐馆"""

	def __init__(self, restaurant_name, cuisine_type):
		"""初始化餐馆的名称和菜系特色"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0		# 设置就餐人数为默认值

	def describe_restaurant(self):
		"""输出餐馆的基本信息"""
		print("\n餐馆信息：")
		print(f"餐馆名称：{self.restaurant_name}")
		print(f"菜系特色：{self.cuisine_type}")

	def open_restaurant(self):
		"""表示餐馆目前正在营业。"""
		print(f"这家{self.restaurant_name}正在营业中。")

	def served_number(self):
		"""打印餐馆目前的就餐人数"""
		print(f"这家餐馆目前有{self.number_served}人就餐。")

	def set_number_served(self, people):
		"""设置就餐的人数"""
		self.number_served = people

	def increment_number_served(self, increment):
		"""递增这家餐馆的就餐人数"""
		if increment >= 0:
			self.number_served += increment
			if self.number_served >= 100:
				print(f"注意：每天可能接待的就餐人数已满，当前的就餐人数为：{self.number_served}")
		else:
			print("递增人数不能为负数！")
	

	

# 创建实例
restaurant = Restaurant("民族饭店", "西北菜")

"""
# 打印属性
print("参观名称：", restaurant.restaurant_name)
print("菜系特色：", restaurant.cuisine_type)
"""

# 调用方法
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 修改就餐人数
restaurant.number_served = 20
restaurant.served_number()

# 设置就餐人数
restaurant.set_number_served(30)
restaurant.served_number()

# 模拟递增的就餐人数
restaurant.increment_number_served(10)
restaurant.served_number()

restaurant.increment_number_served(100)
restaurant.served_number()

"""
# 创建三个实例，并对每个实例调用方法describe_restaurant()。
restaurant1 = Restaurant("北京烤鸭店", "中式正餐")
restaurant2 = Restaurant("麦当劳", "西式快餐")
restaurant3 = Restaurant("上海外婆家", "江浙菜")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
"""