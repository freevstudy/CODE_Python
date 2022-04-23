"""
关于类的练习
创建一个名为Restaurant的类，其方法__init()__设置两个属性：restaurant_name和cuisine_type。
创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法。
其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
根据这一类创建一个名为restaurant的实例，分别打印两个属性，再调用前述两个方法。
再创建三个实例，并对每个实例调用方法describe_restaurant()。
增加餐馆的就餐人数

Date: 2022-04-23
"""

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """初始化饭店的属性"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name.title() + "是一家" + self.type + "。")

    def open_restaurant(self):
        print(self.name.title() + "正在营业中。")

    def dinner_number(self):
        """打印一条指出餐馆里又多少人吃饭的消息"""
        print("这家餐馆有" + str(self.number_served) + "人在里面吃饭。")

    def set_number_served(self, number):
        """设置就餐人数"""
        self.number_served = number

    def increment_number_served(self, add_number):
        """增加就餐人数"""
        self.number_served += add_number
    
    def think_dinner_number(self):
        print("我认为这家餐馆每天最多能接待" + str(self.number_served) + "人。")

restaurant = Restaurant('老盛昌', '面食店')
restaurant.describe_restaurant()

restaurant.set_number_served(300)
restaurant.dinner_number()

restaurant.increment_number_served(50)
restaurant.think_dinner_number()
