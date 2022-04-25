### 练习1 判断闰年
请编写一个判断闰年或平年的程序，运行后由用户输入一个整数（比如2008），然后自动输出类似 “2008是闰年” 的信息。

闰年的判断方法为：如果一个数字可以被4整除，同时不能被100整除，那么这一年就是闰年。但是，如果这个数字可以被400整除，那么它仍然是闰年。
```python
year = int(input('请输入年份：'))

if year % 4 == 0 and year % 100 != 0:
    print(str(year) + "年是闰年。")
elif year % 400 == 0:
    print(str(year) + "年是闰年。")
else:
    print(str(year) + "年是平年。")
```
### 练习2 判断月份
请编写一个程序完成月份转换，输入上半年的整数月份，打印转换后的季度与月份信息。例如：

输入数字3，则打印"第一季度 三月"；
输入数字5，则打印"第二季度 五月"；
输入其他数字，则打印"其他季度"。
```python
month = int(input('请输入月份：'))

if month == 1:
    print("第一季度 一月")
elif month == 2:
    print("第一季度 二月")
elif month == 3:
    print("第一季度 三月")
elif month == 4:
    print("第二季度 四月")
elif month == 5:
    print("第二季度 五月")
elif month == 6:
    print("第二季度 六月")
elif 6 < month <= 12:
    print("其他季度")
else:
    print("输入的月份不合法，请重新输入。")
```
### 练习3 比较大小
输入三个不同的整数值a, b和c。使用分支语句判断并打印最大值
```python
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a == b or b == c or a == c:
    print("必须是不同的值，请重新输入。")
elif a > b and a > c:
    print(str(a) + "是最大值。")
elif b > a and b > c:
    print(str(b) + "是最大值。")
elif c > b and c > a:
    print(str(c) + "是最大值。")
```
# 练习4 游戏评价
请输入玩家的得分，判断玩家最后的等级评价：

0~200    评价为C；

201~500  评价为B；

501~1200 评价为A；

1200以上  评价为S。
```python
score = int(input('请输入得分：'))

if 0 <= score <= 200:
    assess = 'C'
elif 201 <= score <= 500:
    assess = 'B'
elif 501 <= score <= 1200:
    assess = 'A'
elif score > 1200:
    assess = 'S'

print("你的最终评价为：" + assess)
```
### 练习5 图形判断
输入三条线段的长度，判断它们是否可以构成一个三角形。
提示：三条线段中任意两条线段长度的和大于第三条线。
```python
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if (a + b) > c or (b + c) > a or (a + c) > b:
    print("这三条线段可以组成一个三角形。")
else:
    print("这三条线段不能组成一个三角形。")
```
### 练习6 分数计算
输入玩家所消灭的敌人个数，判断当前玩家需要增加的分数：
数量在1~20之间增加100分；

数量在21~30之间增加200分；

数量在31~40之间增加400分；

数量高于40增加1000分。

其他情况提示“敌人个数异常”
```python
nums = int(input('消灭敌人的个数：'))

if 1 <= nums <= 20:
    score = 100
elif 21 <= nums <= 30:
    score = 200
elif 31 <= nums <= 40:
    score = 400
elif nums > 40:
    score = 1000
else:
    print("敌人个数异常。")

print("你增加的分数是" + str(score) + "分。")
```
### 练习7 账户权限
输入用户的编号（1~1000）和权限等级（1~3）：

要求：

如果权限等级是1则提示“无权限访问”；

如果等级是2则提示“可读权限”；

如果等级是3则提示“读写权限”；

其他等级提示“权限异常”。

当权限是2或3时，用户编号在100~1000之间，根据用户的编号显示对应的文件信息：

例如编号是100，显示“文件： 100”，如果超出用户编号范围则显示“编号异常”。
```python
grade = int(input('请输入权限等级(1 ~ 3)：'))
number = int(input('请输入用户编号(1 ~ 1000)：'))

if grade == 1:
    print("无权限访问")
elif grade == 2 and 100 <= number <= 1000:
    print("可读权限")
    print("文件：" + str(number))
elif grade == 3 and 100 <= number <= 1000:
    print("读写权限")
    print("文件：" + str(number))
elif number < 100 or number > 1000:
    print("编号异常")
else:
    print("权限异常。")
```
