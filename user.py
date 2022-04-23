"""
关于类的练习
创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介通常会存储的其他几个属性。
在类User中定义一个名为describe_user()的方法，它打印用户信息摘要；
再定义一个名为greet_user()的方法，它向用户发出个性化的问候。
创建多个表示不同用户的实例，并对每个实例都调用上述两个方法
增加登录次数

Date: 2022-04-23
"""

class User():
    def __init__(self, first_name, last_name):
        """初始化用户属性"""
        self.first = first_name
        self.last = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("用户名称为：" + self.first + self.last)
        print("登录用户量：(重置中......)" + str(self.login_attempts))

    def greet_user(self):
            print(self.first + self.last + "你好，欢迎登录此系统！")

    def increment_login_attempts(self, add):
        self.login_attempts =+ add
        print("登录用户量：" + str(self.login_attempts))

    def reset_login_attempts(self):
        self.login_attempts = 0
        
user = User('吴', '军')
user.increment_login_attempts(1)
user.increment_login_attempts(1)
user.increment_login_attempts(1)
user.reset_login_attempts()
user.describe_user()