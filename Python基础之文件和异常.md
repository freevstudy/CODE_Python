10-1 在文本编辑器中新建一个文件，写几句话来总结一下你至此学到的的Python知识，其中每一行都以“In Python you can”打头。将这个文件命名为learning_python.txt，并将你缩写的内容打印三次：

**learning_python.txt**

---
In Python you can 用列表、字典、类描述一个现实世界中具体的事物

In Python you can 用循环执行重复的代码

In Python you can 用判断语句让程序有一定的判断能力

---

第一次打印时读取整个文件；
```python
filename = 'learning_python.txt'

with open(filename, encoding='utf-8') as file_object:
    message = file_object.read()
    print(message)
```
第二次打印时遍历文件对象；
```python
filename = 'learning_python.txt'

with open(filename, encoding='utf-8') as file_object:
    for message in file_object:
        print(message.rstrip())
```
第三次打印时将各行存储在一个列表中，再用with代码外打印它们。
```python
filename = 'learning_python.txt'

with open(filename, encoding='utf-8') as file_object:
    messages = file_object.readlines()

for message in messages:
    print(message.rstrip())
```
10-2 读取你刚创建的文件learning_python.txt中的每一行，将其中的Python都替换为另一门语言的名称，如C。将修改后的各行都打印到屏幕上。
```python
filename = 'learning_python.txt'

with open(filename, encoding='utf-8') as file_object:
    messages = file_object.readlines()

for message in messages:
    message = message.replace('Python', 'C')
    print(message.rstrip())
```
10-3 编写一个程序，提示用户输入其名字；用户做出响应后，将其名字写入到文件guest.txt中。
```python
filename = 'guest.txt'

guests = input("请输入您的名字：")
with open('guest.txt', 'w', encoding='utf-8') as file_object:
    file_object.write(guests)
```
10-4 编写一个while循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件guest_book.txt中。确保这个文件中的每条记录都独占一行。
```python
filename = 'guest_book.txt'

while True:
    guests = input("请输入您的姓名：")
    if guests == '':
        break
    else:
        print("很高兴看到您，" + guests)
    with open('guest_book.txt', 'a', encoding='utf-8') as file_object:
        file_object.write(guests + "\n")
```
10-5 编写一个while循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
```python
filename = 'reasons.txt'

while True:
    reasons = input("您为什么喜欢编程？\n")
    if reasons == '':
        break
    with open('reasons.txt', 'a', encoding='utf-8') as file_object:
        file_object.write(reasons + "\n")
```
10-6 提示用户提供数值输入时，常出现的一个问题时，用户提供的时文本而不是数字。在这种情况下，当你尝试将输入转换为整数时，将引发TypeError异常。编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。在用户输入的任何一个之不是数字时都捕获TypeError异样，并打印一条友好的错误消息。对你编写的程序进行测试：先输入两个数字，再输入一些文本而不是数字。
```python
try:
    a = int(input("a = "))
    b = int(input("b = "))
except ValueError:
    print("请输入数字！")
else:
    sum = a + b
    print("Sum = ", sum)
```
10-7 将你为完成练习10-6而编写的代码放上一个while循环，让用户犯错（输入的是文本而不是数字）后能够继续输入数字。
```python
print("请输入两个数字，程序会将两个数字相加。")
print("当输入'q'时，程序会退出。")

while True:
    a = input("\na = ")
    if a == 'q':
        break
    b = input("b = ")
    if b == 'q':
        break
    try:
        sum = int(a) + int(b)
    except ValueError:
        print("请输入数字！")
    else:
        print("Sum = ", sum)
```
10-8 创建两个文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。将这些代码放在一个try-except代码块中，以便在文件不存在时捕获FileNotFound错误，并打印一条友好的消息。将其中一个文件移到另一个地方，并确认except代码块中的代码将正确地执行。

**创建cats.txt**
```python
filename = 'cats.txt'

with open('cats.txt', 'w', encoding='utf-8') as file_object:
    file_object.write("毛毛\n")
    file_object.write("鸡腿儿\n")
    file_object.write("小饭团")
```
**创建dogs.txt**
```python
filename = 'dogs.txt'
with open('dogs.txt', 'w', encoding='utf-8') as file_object:
    file_object.write("歪歪\n")
    file_object.write("胡巴\n")
    file_object.write("旺财")
```
**读取文件并显示**
```python
def read_txt(filename):
    """读取文件并显示"""
    with open(filename, encoding='utf-8') as file_object:
        contents = file_object.read()
        print(contents)
    
filenames = ['dogs.txt', 'cats.txt']
for filename in filenames:
    read_txt(filename)
```
**加入异常处理代码块**
```python
def read_txt(filename):
    """读取文件并显示"""
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
            print(contents)
    except FileNotFoundError:
        msg = "文件" + filename + "不存在。"
        print(msg)
    
filenames = ['dogs.txt', 'cats.txt']
for filename in filenames:
    read_txt(filename)
```
10-9 修改你在练习10-8中编写的except代码块，让程序在文件不存在时一言不发。
```python
def read_txt(filename):
    """读取文件并显示"""
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
            print(contents)
    except FileNotFoundError:
        pass
    
filenames = ['dogs.txt', 'cats.txt']
for filename in filenames:
    read_txt(filename)
```
10-10 访问项目Gutenberg，并找一些你想分析的图书。下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。
编写一个程序，它读取你在项目Guteberg中获取的文件，并计算单词‘the'在每个文件中分别出现了多少次。
```python
filename = 'Network of Crime.txt'

try:
    with open(filename, encoding='utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + "does not exist."
    print(msg)
else:
    words = contents.lower().count('the') 
    print("The file " + filename + " has about " + str(words) + " 'the' words.")
```
10-11 编写一个程序，提示用户输入他喜欢的数字，并使用json.dump()将这个数字存储到文件中。再编写一个程序，从文件中读取这个值，并打印消息“I know your favorite number! It's:"。
```python
import json

number = input("Please enter the number you like: ")

filename = 'favorite_nubmer.json'
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)

with open(filename) as f_obj:
    number = json.load(f_obj)

print("I know your favorite number! It's " + number + '.')
```
10-12 将练习10-11中的两个程序合而为一。如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入她喜欢的数字并将其存储到文件中。运行这个程序两次，看看它是否向预期的那样工作。
```python
import json

filename = 'favorite_nubmer.json'
try:
    with open(filename) as f_obj:
        favorite_number = json.load(f_obj)
except:
    favorite_number = input("Please enter the number you like: ")
    with open(filename, 'w') as f_obj:
        json.dump(favorite_number, f_obj)
        print("The number you store is " + favorite_number + ".")
else:
    print("I know your favorite number! It's " + favorite_number + ".")
```
10-13 最后一个remember_me.py版本假设用户要么已输入其用户名，要么是首次运行该程序。我们应修改这个程序，以应对这样的情形：当前和最后一次运行该程序的用户并非同一个人。

为此，再greet_user()中打印欢迎用户回来的消息前，先询问他用户名是否是对的。如果不对，就调用get_new_username()让用户输入正确的用户名
```python
import json

def get_stored_username():
    """如果存储了用户名就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        result = input("Is " + username + " your name? ")
        if result == 'yes':
            print("Welcome back, " + username + "!")
        else:        
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
        
greet_user()
```
