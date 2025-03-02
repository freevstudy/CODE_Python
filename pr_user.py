class User:
    """有关用户信息的类"""

    def __init__(self, first_name, last_name, age, gender, occupation, location):
        """初始化用户的属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.location = location

    def describe_user(self):
        """显示用户的基本信息"""
        print("\n=== 用户信息摘要 ===")
        print(f"姓名：{self.first_name}{self.last_name}")
        print(f"年龄：{self.age}")
        print(f"性别：{self.gender}")
        print(f"职业：{self.occupation}")
        print(f"居住地：{self.location}")

    def greet_user(self):
        """向用户发出问候"""
        print(
            f"\n你好，{self.first_name}{self.last_name}！欢迎回来，祝你在{self.location}生活愉快！"
        )


# 创建三个用户实例
user1 = User("张", "伟", 28, "男", "软件工程师", "北京")
user2 = User("李", "娜", 32, "女", "数据分析师", "上海")
user3 = User("王", "小明", 45, "男", "项目经理", "广州")

# 展示用户信息并发送问候
for user in [user1, user2, user3]:
    user.describe_user()
    user.greet_user()
    print("-" * 40)
