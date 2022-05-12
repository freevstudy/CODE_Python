9-1 创建一个名为Restaurant的类，其方法__init__()设置两个属性：restaurant_name和cuisine_type。创建一个名为describe_restaurant()的方法和一个名为open_restaurant()方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。

根据这个类创建一个名为restaurant的实例，分别打印其两个属性，在调用前述两个方法。
```python
class Restaurant():
    """餐馆的基本情况"""

    def __init__(self, restaurant_name, cuisine_type):
        """餐馆属性的初始化"""
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """餐馆的名字和类型"""
        print(self.name + "是一家" + self.type + "。")

    def open_restaurant(self):
        """餐馆的营业状态"""
        print(self.name + "目前正在营业中。")

restaurant = Restaurant('苏州老盛昌', '面食店')

restaurant.describe_restaurant()
restaurant.open_restaurant()
```
9-2 根据9-1的程序创建三个实例，并对每个实例调用方法describe_restaurant()。
```python
class Restaurant():
    """餐馆的基本情况"""

    def __init__(self, restaurant_name, cuisine_type):
        """餐馆属性的初始化"""
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """餐馆的名字和类型"""
        print(self.name + "是一家" + self.type + "。")

    def open_restaurant(self):
        """餐馆的营业状态"""
        print(self.name + "目前正在营业中。")

restaurant_01 = Restaurant('苏州老盛昌', '面食店')
restaurant_02 = Restaurant('肯德基', '快餐店')
restaurant_03 = Restaurant('紫苑鸡', '熟食店')

restaurant_01.describe_restaurant()
restaurant_02.describe_restaurant()
restaurant_03.describe_restaurant()
```
9-3 创建一个名为User的类，其中包含属性first_name和last_name, 还有用户简介通常会存储的其他几个属性。 在类User中定义一个名为describe_user()的方法，它打印用户信息摘要；再定义一个名为greet_user()的方法，它向用户发出个性化的的问候。

创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
```python
class User():
    """用户信息"""

    def __init__(self, first_name, last_name, user_gender):
        """初始化用户信息"""
        self.first = first_name
        self.last = last_name
        self.gender = user_gender

    def describe_user(self):
        """信息摘要"""
        print("First name: " + self.first)
        print("Last name: " + self.last)
        print("Gender: " + self.gender)

    def greet_user(self):
        """个性化问候"""
        if self.gender == "男性":
            print(self.first + "先生，欢迎登陆本系统。\n")
        elif self.gender == "女性":
            print(self.first + "女士，欢迎登陆本系统。\n")

user_01 = User('李', '艳', '女性')
user_02 = User('王', '大同', '男性')

user_01.describe_user()
user_01.greet_user()
user_02.describe_user()
user_02.greet_user()
```
9-4 根据9-1编写的程序，添加一个名为number_served的属性，并将其默认值设置为0.根据这个类创建一个名为restaurant的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。

添加一个名为set_number_served()的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。

添加一个名为increment_number_served()的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
**就餐人数为初始值时**
```python
class Restaurant():
    """餐馆的基本情况"""

    def __init__(self, restaurant_name, cuisine_type):
        """餐馆属性的初始化"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """餐馆的名字和类型"""
        print(self.name + "是一家" + self.type + "。")

    def open_restaurant(self):
        """餐馆的营业状态"""
        print(self.name + "目前正在营业中。")

    def number(self):
        """指出这家餐馆有多少人就餐"""
        print("这家餐馆目前有" + str(self.number_served) + "人吃饭。")

restaurant = Restaurant('苏州老盛昌', '面食店')

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number()
```
**直接修改就餐人数**
```python
class Restaurant():
    """餐馆的基本情况"""

    def __init__(self, restaurant_name, cuisine_type):
        """餐馆属性的初始化"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """餐馆的名字和类型"""
        print(self.name + "是一家" + self.type + "。")

    def open_restaurant(self):
        """餐馆的营业状态"""
        print(self.name + "目前正在营业中。")

    def number(self):
        """指出这家餐馆有多少人就餐"""
        print("这家餐馆目前有" + str(self.number_served) + "人吃饭。")

restaurant = Restaurant('苏州老盛昌', '面食店')

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served = 300
restaurant.number()
```
**编写方法修改就餐人数的值**
```python
class Restaurant():
    """餐馆的基本情况"""

    def __init__(self, restaurant_name, cuisine_type):
        """餐馆属性的初始化"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """餐馆的名字和类型"""
        print(self.name + "是一家" + self.type + "。")

    def open_restaurant(self):
        """餐馆的营业状态"""
        print(self.name + "目前正在营业中。")

    def number(self):
        """指出这家餐馆有多少人就餐"""
        print("这家餐馆目前有" + str(self.number_served) + "人吃饭。")
    
    def set_number_served(self, set_number):
        """设置就餐的人数"""
        self.number_served = set_number

restaurant = Restaurant('苏州老盛昌', '面食店')

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(300)
restaurant.number()
```
**增加就餐人数**
```python
class Restaurant():
    """餐馆的基本情况"""

    def __init__(self, restaurant_name, cuisine_type):
        """餐馆属性的初始化"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """餐馆的名字和类型"""
        print(self.name + "是一家" + self.type + "。")

    def open_restaurant(self):
        """餐馆的营业状态"""
        print(self.name + "目前正在营业中。")

    def number(self):
        """指出这家餐馆有多少人就餐"""
        print("这家餐馆目前有" + str(self.number_served) + "人吃饭。")
    
    def set_number_served(self, set_number):
        """设置就餐的人数"""
        self.number_served = set_number

    def increment_number_served(self, add_number):
        """增加就餐人数"""
        self.number_served += add_number
        print("我认为这家餐馆最多能容纳" + str(self.number_served) + "人吃饭。")

restaurant = Restaurant('苏州老盛昌', '面食店')

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(300)
restaurant.number()
restaurant.increment_number_served(200)
```
9-5 根据9-3编写的程序，添加一个名为login_attempts的属性。编写一个名为increment_login_attempts()的方法，它将属性login_attempts的值加1。再编写一个名为reset_login_attempts()的方法，它将属性login_attempts的值重置为0。

根据User类创建一个实例，再调用方法increment_login_attempts()多次。打印属性login_attempts的值，确认它被正确地递增；然后，调用方法reset_login_attempts()。并再次打印属性login_attempts的值，确认它被重置为0。
```python
class User():
    """用户信息"""

    def __init__(self, first_name, last_name, user_gender):
        """初始化用户信息"""
        self.first = first_name
        self.last = last_name
        self.gender = user_gender
        self.login_attempts = 0

    def describe_user(self):
        """信息摘要"""
        print("First name: " + self.first)
        print("Last name: " + self.last)
        print("Gender: " + self.gender)

    def greet_user(self):
        """个性化问候"""
        if self.gender == "男性":
            print(self.first + "先生，欢迎登陆本系统。\n")
        elif self.gender == "女性":
            print(self.first + "女士，欢迎登陆本系统。\n")
    
    def increment_login_attempts(self):
        """递增登录次数"""
        self.login_attempts += 1
        print("已登录" + str(self.login_attempts) + "次。")

    def reset_login_attempts(self):
        """重置登录次数"""
        self.login_attempts = 0
        print("登录次数已重置为" + str(self.login_attempts) + "次。")

user = User('李', '艳', '女性')
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()
```
9-6 冰淇凌小店是一种特殊的餐馆。编写一个名为IceCreamStand的类，让它继承你为完成练习 9-1或练习9-4而编写的Restaurant类。这两个版本的Restaurant类都可以，挑选你更喜欢的那个即可。添加一个名为flavors的属性，用于存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个IceCreamStand实例，并调用这个方法。
```python
class Restaurant():
    """餐馆的基本情况"""

    def __init__(self, restaurant_name, cuisine_type):
        """餐馆属性的初始化"""
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """餐馆的名字和类型"""
        print(self.name + "是一家" + self.type + "。")

    def open_restaurant(self):
        """餐馆的营业状态"""
        print(self.name + "目前正在营业中。")

class IceCreamStand(Restaurant):
    """冰淇淋小店"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化冰淇凌的口味"""

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['草莓味', '巧克力味', '柠檬味']

    def descreibe_icecream(self):
        """打印冰淇凌店的口味"""
        
        print("它生产的口味有：")
        for self.flavor in self.flavors:
            print(self.flavor)
            
restaurant = IceCreamStand('蜜糖冰城', '冰淇凌店')

restaurant.describe_restaurant()
restaurant.descreibe_icecream()
```
9-7 管理员是一种特殊的用户。编写一个名为Admin的类，让它继承你为完成练习9-3或练习9-5而编写的User类。添加一个名为privileges的属性，用于存储一个由字符串（如“can add post”、“can delete post”、“can ban user”等）组成的列表。编写一个名为show_privileges()的方法，它显示管理员的权限。创建一个Admin实例，并调用这个方法。
```python
class User():
    """用户信息"""

    def __init__(self, first_name, last_name, user_gender):
        """初始化用户信息"""
        self.first = first_name
        self.last = last_name
        self.gender = user_gender

    def describe_user(self):
        """信息摘要"""
        print("First name: " + self.first)
        print("Last name: " + self.last)
        print("Gender: " + self.gender)

    def greet_user(self):
        """个性化问候"""
        if self.gender == "男性":
            print(self.first + "先生，欢迎登陆本系统。\n")
        elif self.gender == "女性":
            print(self.first + "女士，欢迎登陆本系统。\n")

class Admin(User):
    """管理员"""

    def __init__(self, first_name, last_name, user_gender):
        """初始化用户"""

        super().__init__(first_name, last_name, user_gender)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """显示用户权限"""

        print("你是管理员，有如下权限：")
        for self.privilege in self.privileges:
            print(self.privilege)

user = User('王', '大同', '男性')
user.describe_user()
user.greet_user()

admin = Admin('王', '大同', '男性' )
admin.show_privileges()
```
9-8 编写一个名为Privileges的类，它只有一个属性——privileges，其中存储了练习9-7所说的字符串列表。将方法show_privileges()移到这个类中。在Admin类中，将一个Privileges实例用作其属性。创建一个Admin实例，并使用方法show_privileges()来显示其权限。
```python
class User():
    """用户信息"""

    def __init__(self, first_name, last_name, user_gender):
        """初始化用户信息"""
        self.first = first_name
        self.last = last_name
        self.gender = user_gender

    def describe_user(self):
        """信息摘要"""
        print("First name: " + self.first)
        print("Last name: " + self.last)
        print("Gender: " + self.gender)

    def greet_user(self):
        """个性化问候"""
        if self.gender == "男性":
            print(self.first + "先生，欢迎登陆本系统。\n")
        elif self.gender == "女性":
            print(self.first + "女士，欢迎登陆本系统。\n")

class Privileges():
    """权限"""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """显示用户权限"""

        print("你是管理员，有如下权限：")
        for self.privilege in self.privileges:
            print(self.privilege)

class Admin(User):
    """管理员"""

    def __init__(self, first_name, last_name, user_gender):
        """初始化用户"""

        super().__init__(first_name, last_name, user_gender)
        self.privileges = Privileges()
    
user = User('王', '大同', '男性')
user.describe_user()
user.greet_user()

admin = Admin('王', '大同', '男性' )
admin.privileges.show_privileges()
```
9-9 在本节最后一个electric_car.py版本中，给Battery类添加一个名为upgrade_battery()的方法。这个方法检查电瓶容量，如果它不是85，就将它设置为85。创建一辆电瓶容量为默认值的电动汽车，调用方法get_range()，然后对电瓶进行升级，并再次调用get_range(）。你会看到这俩汽车的续航里程增加了。
```python
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表的读数设置为指定的值
        禁止将里程表读数往回调
        """        
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def upgrade_battery(self):
        """升级电瓶"""

        if self.battery_size != 85:
            self.battery_size = 85

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        self.upgrade_battery()
            
class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
my_tesla.battery.get_range()
```
9-13 使用OrderDict类写一个词汇表程序。
```python
from collections import OrderedDict

word_list = OrderedDict()

word_list['world'] = '世界'
word_list['beauty'] = '美好'

for word, explain in word_list.items():
    print(word + ":\n\t" + explain)
```
9-14 模块random包含以各种方式生成随机数的函数，其中的randint()返回一个位于指定范围内的整数，例如，下面的代码返回一个1~6内的整数：

---
from random import randint

x = randint(1, 6)

---

请创建一个Die类，它包含一个名为sides的属性，该属性的默认值为6。编写一个名为roll_die()的方法，它打印位于1和骰子面数之间的随机数。创建一个6面的骰子，再掷10次。

创建一个10面的骰子和一个20面的骰子，并将它们都掷10次。
```python
from random import randint

class Die():

    def __init__(self):
        self.sides = 6

    def roll_die(self):       
        x = randint(1, 6)
        self.sides = x
        print(self.sides)
    
    def roll_die10(self):
        x = randint(1, 10)
        self.sides = x
        print(self.sides)
    
    def roll_die20(self):
        x = randint(1, 20)
        self.sides = x
        print(self.sides)

die = Die()
print("--------6 sides--------")
for i in range(10):
    die.roll_die()

print("--------10 sides--------")
for i in range(10):
    die.roll_die10()

print("--------20 sides--------")
for i in range(10):
    die.roll_die20()
```