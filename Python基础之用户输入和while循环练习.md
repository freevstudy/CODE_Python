7-1 编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，如“Let me see if I can find you a Subaru.”
```python
rents = input("What kind of car would you like to rent? ")
print("Let me see if I can find you a " + rents + ".")
```
7-2 编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌。
```python
number = input("请问共有多少人来此用餐？ ")
number = int(number)

if number > 8:
    print("\n对不起，现在没有空桌。")
else:
    print("\n欢迎光临，现在有空桌。")
```
7-3 让用户输入一个数字，并指出这个数字是否是10的整数倍。
```python
number = input("请输入一个整数：")
number = int(number)

if number % 10 == 0:
    print("\n" + str(number) + "是10的整数倍。")
else:
    print("\n" + str(number) + "不是10的整数倍。")
```
7-4 编写一个循环，提示用户输入一系列比萨配料，并在用户输入'quit'时结束循环。每当用户输入一种配料后，都打印一条消息，说我们会在比萨种添加这种配料。
```python
temp = "\n请输入你需要的配料。"
temp += "\n(当您输入'quit'的时候会退出系统。) "

message = ''
while message != 'quit':
    message = input(temp)
    if message != 'quit':
        print("我们会在比萨中添加" + message + "。")
```
7-5 有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3~12岁的观众为10美元；超过12岁的观众为15美元。请编写一个循环，在其中询问用户的年龄，并指出其票价
```python
temp = "\n请输入您的年龄，我们会根据您的年龄给出不同的票价。"
temp += "\n(当输入-1时会退出系统。) "

age = 0
while age != -1:
    age = int(input(temp))

    if age != -1:
        if age < 3:
            print("您的年龄小于3岁，免费观看。")
        elif 3 <= age <= 12:
            print("您的年龄介于3~12岁，票价为10美元。")
        elif age > 12:
            print("您已经超过12岁，票价为15美元。")
```
7-6 以另一种方式完成练习7-4或7-5：
- 使用变量active来控制循环结束的时机
- 使用break语句在用户输入'quit'时退出循环
```python
# 7-4 使用active变量控制循环结束
temp = "\n请输入你需要的配料。"
temp += "\n(当您输入'quit'的时候会退出系统。) "

active = True
while active:
    message = input(temp)

    if message == 'quit':
        active = False
    else:
        print("我们会在比萨中添加" + message + "。")
```
```python
# 7-4 使用break语句在用户输入'quit'时退出循环
temp = "\n请输入你需要的配料。"
temp += "\n(当您输入'quit'的时候会退出系统。) "

active = True
while active:
    message = input(temp)

    if message == 'quit':
        active = False
    else:
        print("我们会在比萨中添加" + message + "。")
```
```python
# 7-5 使用active变量控制循环结束
temp = "\n请输入您的年龄，我们会根据您的年龄给出不同的票价。"
temp += "\n(当输入'quit'时会退出系统。) "

active = True
while active:
    age = input(temp)

    if age == 'quit':
        active = False
    elif int(age) < 3:
        print("您的年龄小于3岁，免费观看。")
    elif 3 <= int(age) <= 12:
        print("您的年龄介于3~12岁，票价为10美元。")
    elif int(age) > 12:
        print("您已经超过12岁，票价为15美元。")
```
```python
# 7-5 使用break语句在用户输入'quit'时退出循环
temp = "\n请输入您的年龄，我们会根据您的年龄给出不同的票价。"
temp += "\n(当输入'quit'时会退出系统。) "

age = ''
while age != 'quit':
    age = input(temp)

    if age == 'quit':
        break
    elif int(age) < 3:
        print("您的年龄小于3岁，免费观看。")
    elif 3 <= int(age) <= 12:
        print("您的年龄介于3~12岁，票价为10美元。")
    elif int(age) > 12:
        print("您已经超过12岁，票价为15美元。")
```
7-8 创建一个名为sandwich_orders的列表，在其中包含各种三明治的名字；再创建一个名为finished_sandwich的空列表。
遍历列表sandwich_orders,对于其中的每种三明治，都打印一条消息，如I made your tuna sandwich, 将这些三明治列出来。
```python
sandwich_orders = ['蔬菜沙拉三明治', '猪排三明治', '培根三明治']
finished_sandwiches = []

while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print("已经制作好" + made_sandwich + "了。")
    finished_sandwiches.append(made_sandwich)

print("\n已经做好的三明治：")
for finished_sandwich in finished_sandwiches:
    print("\t" + finished_sandwich)
```
7-9 在7-8练习的基础上，列表增加五香烟熏牛肉三明治，打印一条消息声明已卖完，并且将列表中的五香烟熏牛肉三明治删除。
```python
sandwich_orders = ['五香牛肉烟熏三明治', '蔬菜沙拉三明治', '五香牛肉烟熏三明治', '猪排三明治', '培根三明治', '五香牛肉烟熏三明治']
finished_sandwiches = []

print("对不起，本店的五香牛肉烟熏三明治已卖完。\n")
while '五香牛肉烟熏三明治' in sandwich_orders:
    sandwich_orders.remove('五香牛肉烟熏三明治')

while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print("已经制作好" + made_sandwich + "了。")
    finished_sandwiches.append(made_sandwich)

print("\n已经做好的三明治：")
for finished_sandwich in finished_sandwiches:
    print("\t" + finished_sandwich)
```
7-10 编写一个程序，调查用户梦想的度假胜地。使用类似与“If you could visit one place in the world, where you go?”的提示。并编写一个打印调查结果的的代码块
```python
places = {}
polling_active = True

while polling_active:
    name = input("\n您的姓名： ")
    questions = input("您梦想中的度假胜地是哪里？ ")

    places[name] = questions

    repeat = input("\n在场的各位还有要做调查的吗？(y / n) ")
    if repeat == 'n':
        polling_active = False

print("--- 调查结果 ---")
for name, place in places.items():
    print(name + "的梦想度假胜地是" + place + "。")
```
