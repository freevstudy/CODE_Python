"""
关于类的练习
创建一个名为Restaurant的类，其方法__init()__设置两个属性：restaurant_name和cuisine_type。
创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法。
其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
根据这一类创建一个名为restaurant的实例，分别打印两个属性，再调用前述两个方法。

Date: 2022-04-21
"""

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """初始化饭店的属性"""
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(self.name.title() + "是一家" + self.type + "。")

    def open_restaurant(self):
        print(self.name.title() + "正在营业中。")

restaurant = Restaurant('老盛昌汤包', '面食店')
print(restaurant.name)
print(restaurant.type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
