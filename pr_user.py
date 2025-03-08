"""
创建一个名为User的类，其中包含属性first_name和last_name，以及用户简介通常会存储的其他几个属性。
在类User中定义一个名为describe_user()的方法，用于打印用户信息摘要。
再定义一个名为greet_user()的方法，用于向用户发出个性化的问候。

创建多个表示不同用户的实例，并对每个实例调用上述两个方法。
添加一个名为login_attempts的属性。编写一个名为increment_login_attempts()的方法，将属性login_attempts的值加1。再编写一个名为reset_login_attempts()的方法，将属性login_attempts的值重置为0。
根据User类创建一个实例，再调用方法increment_login_attempts()多次。打印属性login_attempts的值，确认它被正确地递增。然后，调用方法reset_login_attempts()，并再次打印属性login_attempts的值，确认它被重置为0。
"""


class User:
    """创建一个用户基本信息的类"""

    def __init__(
        self, first_name, last_name, gender, age, occupation, location, login_attempts=0
    ):
        """初始化用户的基本信息"""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.occupation = occupation
        self.location = location
        self.login_attempts = login_attempts  # 添加登录次数属性

    def describe_user(self):
        """打印用户的信息摘要"""
        print("\n用户信息：")
        print(f"姓名：{self.first_name}{self.last_name}")
        print(f"性别：{self.gender}")
        print(f"年龄：{self.age}岁")
        print(f"职业：{self.occupation}")
        print(f"地址：{self.location}")
        print(f"登录次数：{self.login_attempts}")

    def greet_user(self):
        """向用户发出问候语。"""
        print(
            f"{self.first_name}{self.last_name}, 欢迎回来，希望你在{self.location}度过美好的时光。"
        )

    def increment_login_attempts(self):
        """递增用户的登录次数"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """重置用户的登录次数"""
        self.login_attempts = 0


class Privileges:
    """创建一个权限类"""

    def __init__(self, privileges=None):
        """初始化权限列表。"""
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        """显示管理员的权限。"""
        print("\n管理员的权限：")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """创建一个管理员类，继承自User类。"""

    def __init__(
        self, first_name, last_name, gender, age, occupation, location, login_attempts=0
    ):
        """初始化管理员的基本信息。"""
        super().__init__(
            first_name, last_name, gender, age, occupation, location, login_attempts
        )
        self.privileges = Privileges()  # 使用Privileges类的实例做为属性。


# 创建实例
user1 = User("张", "军", "男", 45, "仓库主管", "嘉定")
user2 = User("兰", "晓薇", "女", 36, "销售主管", "余姚")
user3 = User("王", "小明", "男", 25, "IC设计师", "深圳")

# 创建Admin实例
admin = Admin("李", "明", "男", 37, "系统管理员", "北京")

# 添加权限
admin.privileges.privileges = [
    "can add post",
    "can delete post",
    "can ban user",
    "can edit user",
    "can manage comments",
]

# 调用方法
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

admin.describe_user()
admin.greet_user()
# admin.show_privileges()
admin.privileges.show_privileges()

# 测试登录次数
print("\n测试登录次数：")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.describe_user()

user1.reset_login_attempts()
user1.describe_user()
