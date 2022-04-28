
### 练习1 水仙花数
求解“水仙花数”是一道非常经典的循环练习题。如果一个三位数（ 100 —— 999 ）等于它每一位数字的立方和，则称这个数为“水仙花数”。比如 153 = 1^3 + 5^3 + 3^3，所以 153 就是一个水仙花数。
本题的正确输出结果应当包括四个数字： 153 370 371 407
```python
x = 1
while x <= 9:

    y = 0
    while y <= 9:

        z = 0
        while z <= 9:
            a = x ** 3 + y ** 3 + z ** 3
            b = x * 100 + y * 10 + z

            if a == b:
                print(str(x) + str(y) + str(z) + "是水仙花数。")
            z = z + 1
        
        y = y + 1
    
    x = x + 1
```
### 练习2 多次抽奖
宣读三个中奖号码，中奖号码为5个数字
第一次先播放“一等奖是”，然后随机生成五位中奖号码并播出；第二次先播放“二等奖是”，然后再随机生成中奖号码并播出，如此类推。
```python
import os
import time
import random

i = 1

while i <= 3:
    os.system('d:/Notes/bonus' + str(i) + '.m4a')
    time.sleep(4)

    j = 0
    while j < 5:
        num = random.randint(0, 9)
        fname = 'd:/Notes/' + str(num) + '.m4a'
        os.system(fname)

        time.sleep(4)

        j = j + 1

    i = i + 1
```
### 练习3 打印图形
请使用循环语句打印如下图形：
```
******
********
**********
```
```python
i = 0

while i < 3:
    j = 1

    while j < 6 + 2 * i:
        print("*", end = '')

        j = j + 1
    i = i + 1
    print()
```
### 练习4 学生信息管理系统
请按以下需求编写一个学生信息管理系统，用户可以根据菜单中的编号选择相应的操作：

主菜单：1-添加学生信息 2-修改学生信息 3-清空学生信息 4-打印学生信息 5-退出程序

1. “添加学生信息”选项中要求输入姓名，年龄，班级。添加学生信息后自动进入子菜单。
    
    子菜单：1-文科成绩 2-理科成绩 3-退出

    选择1输入历史、政治和地理成绩并打印成绩；

    选择2输入物理、生物和化学成绩并打印成绩。
2. “修改学生信息”要求显示子菜单，可以重新输入各科的成绩，显示输入后的成绩。

3. “清空学生信息”要求将所有学生信息全部清空为空字符串。

4. “打印学生信息”要求打印学生的所有信息。

5. 选择主菜单“退出”则结束程序。
```python
while True:
    num = input("主菜单：\n1-添加学生信息\n2-修改学生信息\n3-清空学生信息\n4-打印学生信息\n5-退出程序\n")
    
    if num == '1':
        name = input('姓名：')
        age = int(input('年龄：'))
        classes = input('班级：')
        while True:
            temp = input("1-文科成绩\n2-理科成绩\n3-退出\n")
            
            if temp == '1':
                history = float(input('历史成绩：'))
                politics = float(input('政治成绩：'))
                geography = float(input('地理成绩：'))
            elif temp == '2':
                physics = float(input('物理成绩：'))
                biology = float(input('生物成绩：'))
                chemical = float(input('化学成绩：'))
            elif temp == '3':
                break
            else:
                print("输入有误，请重新输入。")
    elif num == '2':
        while True:
            temp = input('1-文科成绩\n2-理科成绩\n3-退出\n')

            if temp == '1':
                history = float(input('历史成绩（已修改）：'))
                politics = float(input('政治成绩（已修改）：'))
                geography = float(input('地理成绩（已修改）：'))
            elif temp == '2':
                physics = float(input('物理成绩（已修改）：'))
                biology = float(input('生物成绩（已修改）：'))
                chemical = float (input('化学成绩（已修改）：'))
            elif temp == '3':
                break
            else:
                print("输入有误，请重新输入。")
    elif num == '3':
        name = age = classes = ''
        history = politics = geography = ''
        physics = biology = chemical = ''
        print("学生信息已清空。")
    elif num == '4':
        print("学生信息")
        print("姓名：", name, " 年龄：", age, " 班级：", classes)
        print("历史：", history, " 政治：", politics, " 地理：", geography)
        print("物理：", physics, " 生物：", biology, " 化学：", chemical)
    elif num == '5':
        print("程序结束。")
        break
    else:
        print("输入有误，请重新输入。")
```