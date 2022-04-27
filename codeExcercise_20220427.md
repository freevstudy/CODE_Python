练习1 语音抽奖
编写一个“自动抽奖并宣读中奖号码”的程序。具体方案如下：
先用windows或苹果系统等自带的“录音机”程序（win7系统在“开始菜单”——“附件”中，win10系统在“开始菜单”的程序列表中可以找到），或手机等其他设备，亲自录下10个音频文件，内容就是“零”到“九”十个数字的读音。将这些音频文件保存在硬盘指定位置，并用数字作为文件名，比如 “3.m4a”。
编写程序，使之能够随机生成5个0到9之间的数字。每生成一个数字，就播放与之对应的那个音频文件，从而实现连续读出五位中奖号码的功能。
```python
import os
import time
import random

i = 0

while i < 5:
    num = random.randint(0, 5)
    fname = 'd:/Notes/' + str(num) + '.m4a'
    os.system(fname)

    time.sleep(4)

    i = i + 1
```
练习2 猜数字游戏
实现一个猜数字游戏，随机生成一个0~5之间的数字作为答案。玩家输入猜测的值进行游戏。
如果玩家猜对了，结束游戏；如果猜错了，可以继续猜数字，玩家累计猜错3次时游戏结束。
```python
import random

notes = random.randint(0, 5)
i = 0

while i < 3:
    i = i + 1
    guess = int(input('请输入一个数字，我们会验证是否与生成的数字一样（0-5）:'))

    if guess != notes:
        print("数量不匹配，请重新输入。")
    else:
        print("数量匹配。")
```
练习3 模拟游戏战斗系统
请根据以下要求完成一个模拟游戏战斗系统的程序，玩家可以多次选择攻击方式，直到怪物死亡。
玩家的技能菜单：1-物理攻击，2-魔法攻击，根据编号选择技能。
玩家的物理攻击力100，魔法攻击力120，怪物的血量700，物理防御力80，魔法防御力75
伤害 = 技能攻击力 * 随机系数 - 防御力
怪物血量 = 总血量 - 伤害
其中随机系数在1.9~2.1之间，2.1为暴击。每次攻击后显示怪物的原始血量和剩余血量，如果发生暴击显示“暴击攻击”。
```python
import random

player_attack_ph = 100
player_attack_mg = 120

monster_hp = 700
monster_defens_ph = 80
monster_defens_mg = 75

while monster_hp > 0:
    print("技能菜单\n1-物理攻击\n2-魔法攻击")
    attack_select = int(input("请选择技能（1-2）："))
    modulus = random.randint(19, 21) / 10

    if attack_select == 1:
        if modulus == 2.1:
            print("暴击攻击")
        harm = player_attack_ph * modulus - monster_defens_ph
    elif attack_select == 2:
        if modulus == 2.1:
            print("暴击攻击")
        harm = player_attack_mg * modulus - monster_defens_mg
    else:
        print("你输入的技能不对，请重新输入。")

    monster_hp = monster_hp - harm
    if monster_hp <= 0:
        print("怪物的血量已为0，恭喜你打赢了怪物。")
        break
    print("怪物血量还剩下：", monster_hp)
```
练习4 定时关机程序
请根据以下要求和关机相关命令，编写一个控制电脑自动关机的程序。
功能菜单：1-设置关机计划 2-取消关机计划 3-立即关机 4-退出
功能1，输入关机延迟秒数，计算机将在输入的秒数之后自动关机；
功能2，取消自动关机的任务；
功能3，再次询问用户是否关机，并提示注意保存数据，输入Y立即关机，输入N取消关机并回到功能菜单；
功能4，程序结束。
延迟关机命令：shutdown -s -t 延迟秒数 
取消关机命令：shutdown -a
```python
import os

while True:
    print("功能菜单：\n1-设置关机计划\n2-取消关机计划\n3-立即关机\n4-退出")
    order = int(input('请输入菜单编号（1-4）：'))

    if order == 1:
        time = input('请输入关机延迟秒数，计算机将在秒数结束后自动关机：')
        os.system('shutdown -s -t ' + time)
        print("关机计划已设置，请及时保存你的资料。")
    elif order == 2:
        os.system('shutdown -a')
        print("关机计划已取消")
    elif order == 3:
        print("立即关机")
        while True:
            x = input('关机前请注意保存数据，你确认立即关机吗（y / n)？')
            if x == 'Y' or x == 'y':
                os.system('shutdown -s -t 00')
                break
            elif x == 'N' or x == 'n':
                print("关机取消")
                break
            else:
                print("请输入Y或N")
    elif order == 4:
        print("程序退出")
        break
    else:
        print("你输入的命令有误，请重新输入。")
```