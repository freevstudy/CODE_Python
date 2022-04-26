### 练习1 重复录入
判断闰年程序，使之能够循环运行：程序启动后用户可以反复多次输入年份，并获知其是否为闰年。只有当用户输入“END”时，程序才结束退出。
```python
print("欢迎进入判断闰年的系统。")
s = 'yes'

while s == 'yes':
    year = int(input('请输入年份：'))

    if year % 4 == 0 and year % 100 != 0:
        print(str(year) + "年是闰年。")
    elif year % 400 == 0:
        print(str(year) + "年是闰年。")
    else:
        print(str(year) + "年是平年。")

    s = input('请问还要输入年份吗（yes / end）?')

print("程序结束！")
```
### 练习2 复利计算
输入本金、利率和最大借款年数，程序将输出从第一年到最大借款年之间每年度的欠款总额，效果如下：
请输入本金：100
请输入年利率：0.2
请输入最大借款年数：5
第 1 年欠款总额为 120
第 2 年欠款总额为 144
第 3 年欠款总额为 172
第 4 年欠款总额为 207
第 5 年欠款总额为 248
```python
capital = float(input('请输入本金：'))
rate = float(input('请输入年利率：'))
max_year = int(input('请输入最大借款年数：'))
year = 1

while year <= max_year:
     arrears = capital * ( 1 + rate) ** year
     print("第", year, "年欠款总额为：%d" %arrears)
     year = year + 1
```
### 练习3 成绩输入统计
循环输入多名学生的成绩，直到输入0结束，计算总成绩
```python
score = 1
total = 0

while score != 0:
    score = float(input('请输入学生的成绩：'))
    total = total + score

print("学生的总成绩是：", total)
```
### 练习4 奇偶求和
求0~100之间的所有偶数之和，奇数之和（包含0和100）
```python
num = 0
sum_even = 0
sum_odd = 0

while 0 <= num <= 100:
    if num % 2 == 0:
        sum_even = sum_even + num
    else:
        sum_odd = sum_odd + num

    num = num + 1

print("（0~100）的偶数之和：", sum_even)
print("（0~100）的奇数之和：", sum_odd)
```
练习5 点餐程序
编程实现一个点餐程序：
1. 显示菜单：1-开水白菜（8元），2-狮子头（12元），3-佛跳墙（25元），4-水晶肴肉（18元）， 5-宫保鸡丁（12元）
2. 用户根据编号每次选择一道菜进行点餐，直到用户输入0退出点餐程序。计算下单的总价。
```python
num_menu = 'run'
price = 0

while num_menu:
    print("菜单\n1-开水白菜（8元）\n2-狮子头（12元）\n3-佛跳墙（25元）\n4-水晶肴肉（18元）\n5-宫保鸡丁（12元）")
    num_menu = int(input('请输入菜的编号：'))
    
    if num_menu == 1:
        price = price + 8
    elif num_menu == 2:
        price = price + 12
    elif num_menu == 3:
        price = price + 25
    elif num_menu == 4:
        price = price + 18
    elif num_menu == 5:
        price = price + 12
    elif num_menu == 0:
        print("点餐结束")
    else:
        print("对不起，你的菜在菜单里没有，请重新点菜。")
        
print("你这次总计消费：", price, "元")
```
### 练习6 毕业人数统计
某高等学校的毕业人数呈逐年上涨的趋势，每年增长20%，
请编程计算从2020年的7000人开始，到哪一年总毕业人数可以到达10万人。
```python
num = 7000
year = 0

while num <= 100000:
    num = num + (num * 0.2)
    year = year + 1

print("从2020年开始，我校到", str((2020 + year)) + "年总毕业人数可以达到10万人。")
```
### 练习7 游戏数据统计
现在有5个游戏场景。在每个游戏场景中需要生成一批同类的敌人。请循环输入5个场景的敌人编号并统计敌人总数，具体要求如下所示：
1. 显示当前游戏场景编号(0~4)，显示敌人种类菜单：0-曼德拉（3只），1-巨像兵（1个），2-双足飞龙（5只），3-独眼巨兽（1只），4-美杜莎（7个）。
2. 根据输入的敌人种类编号（0~4）显示敌人的名称和个数，然后切换下一个场景。如果输入的编号错误则保证场景编号不变，重新输入敌人编号直到编号正确。
3. 计算敌人的总数。
```python
scenes = 0
total = 0

while scenes < 5:
    print("当前游戏场景：", scenes)
    print("敌人信息：\n0-曼德拉（3只）\n1-巨像兵（1个）\n2-双足飞龙（5只）\n3-独眼巨兽（1只）\n4-美杜莎（7只）")
    num = int(input('请输入要生成的敌人编号（0 ~ 4）：'))

    if num == 0:
        print("添加曼德拉3只\n")
        total = total + 3
    elif num == 1:
        print("添加巨像兵1个\n")
        total = total + 1
    elif num == 2:
        print("添加双足飞龙5只\n")
        total = total + 5
    elif num == 3:
        print("添加独眼巨兽1只\n")
        total = total + 1
    elif num == 4:
        print("添加美杜莎7个\n")
        total = total + 7
    else:
        print("编号错误，请重新输入。\n")

    scenes = scenes + 1
    
print("敌人的总数：", total)
```