"""
关于类的练习
创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介通常会存储的其他几个属性。
在类User中定义一个名为describe_user()的方法，它打印用户信息摘要；
再定义一个名为greet_user()的方法，它向用户发出个性化的问候。
创建多个表示不同用户的实例，并对每个实例都调用上述两个方法

Date: 2022-04-21
"""

class User():
    def __init__(self, first_name, last_name, occupation):
        """初始化用户属性"""
        self.first = first_name
        self.last = last_name
        self.occupation = occupation

    def describe_user(self):
        name = self.first + self.last
        print(name + "是一位" + self.occupation + "。")

    def greet_user(self):
        if self.occupation == "学生":
            print(self.first + "同学你好，欢迎登录上课界面。")
        elif self.occupation == "老师":
            print(self.first + "老师你好，欢迎登录学员管理界面。")
        
user_01 = User('吴', '军', '学生')
user_02 = User('朱', '玲玉', '老师')

user_01.describe_user()
user_01.greet_user()
user_02.describe_user()
user_02.greet_user()
