8-1 编写一个名为display_message()的函数，它打印一个句子，指出你在本章学的是什么。调用这个函数，确认显示的小时正确无误。
```python
def display_message():
    """显示一条信息"""
    print("刚刚学到了函数定义和调用的方法。")

display_message()
```
8-2 编写一个名为favorite_book()的函数，其中包含一个名为title的形参。
这个函数打印一条消息，如One of my favorite books is Alice in Wonderland。
调用这个函数，并将一本图书的名称作为实参传递给它。
```python
def favorite_book(title):
    """指出最喜欢的书籍"""
    print("我最喜欢的一本书是" + title + "。")

favorite_book('数学之美')
```
8-3 编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。
这个函数应打印一个句子，概要地说明T恤的尺码和字样。

使用位置实参调用这个函数来制作意见T恤；再使用关键字实参来调用这个函数。
```python
def make_shirt(size, model):
    """T恤的尺码和字样"""
    print("T恤的大小：", size)
    print("T恤的字样：", model)

make_shirt('M', '我爱Python')
make_shirt(model='我爱Python', size='M')
```
8-4 修改make_shirt()，使其在默认情况下制作一件印有字样“I love Python”的大号T恤。
调用这个函数来制作如下T恤：

一件印有默认字样的大号T恤

一件印有默认字样的中号T恤

一件印有其他字样的T恤（尺码无关紧要）
```python
def make_shirt(size, model='I love Python'):
    """T恤的尺码和字样"""
    print("T恤的大小：", size)
    print("T恤的字样：", model)

make_shirt('XXX')
make_shirt('M')
make_shirt(size='M', model='适度用眼 保护视力')
```
8-5 编写一个名为describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。
这个函数应打印一个简单的句子，如Reykjavik is in Iceland。

给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
```python
def describe_city(city_name, nation='中国'):
    """显示一个城市的简单信息"""
    print(city_name + "属于" + nation + "。")

describe_city('大连')
describe_city('深圳')
describe_city(city_name='名古屋', nation='日本')
```
8-6 编写一个名为city_country()的函数，它接受城市的名称及其所属的国家。
这个函数返回一个格式类似与下面这样的字符串：
---
"Santiago, Chile"
---
至少使用三个城市-国家对，调用这个函数，并打印它返回的值。
```python
def city_country(city_name, country):
    """城市-国家对"""
    full_city = city_name + ', ' + country
    return full_city.title()

cityCountry = city_country('shanghai', 'china')
print(cityCountry)
```
8-7 编写一个名为make_album()的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑，并返回一个包含这两项信息的字典。
使用这个函数创建三个不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。

给函数make_album()添加一个可选形参，以便能够存储包含的歌曲数。如果调用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
```python
def make_album(singer, album_name, sing_num=''):
    """歌手名字和专辑名"""
    singer_album = {'singer': singer, 'album_name': album_name}
    if sing_num:
        singer_album['sing_num'] = sing_num
    return singer_album

album = make_album('Alicia Keys', 'Songs In A Minor')
print(album)

album = make_album('郭英男 & 馬蘭吟唱隊', '生命之环')
print(album)

album = make_album('GALA', '追梦痴子心', 12)
print(album)
```
8-8 在8-7的基础上，编写一个while循环，让用户输入以恶专辑的歌手和名称。获取这些信息后，使用它们来调用函数make_album()，并将创建的字典打印出来。在这个while循环中，务必要提供退出途径。
```python
def make_album(singer, album_name, sing_num=''):
    """歌手名字和专辑名"""
    singer_album = {'singer': singer, 'album_name': album_name}
    if sing_num:
        singer_album['sing_num'] = sing_num
    return singer_album

while True:
    print("\n请输入和专辑有关的信息：")
    print("(输入'q'时就会退出。)")
    
    singer_name = input("歌手名字：")
    if singer_name == 'q':
        break

    singer_album = input("专辑名字：")
    if singer_album == 'q':
        break

    album_num = input("请输入专辑歌曲数：")
    if album_num == '':
        album = make_album(singer_name, singer_album)
        print(album)
    elif album_num != '':
        album = make_album(singer_name, singer_album, album_num)
        print(album)
    elif album_num == 'q':
        break
```
8-9 创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians()的函数，这个函数打印列表中每个魔术师的名字。
```python
def show_magicians(magicians_name):
    """显示魔术师的名字"""
    print("\n下面出场的魔术师有：")
    for magician_name in magicians_name:
        print(magician_name)

magicians_name = ['Eric', 'Alice', '刘谦']
show_magicians(magicians_name)
```
8-10 在8-9的基础上，编写一个名为make_great()的函数，对魔术师列表进行修改，在每个魔术师的名字都加入字样“the Great”。调用函数show_magicians()。确认魔术师的列表确实变了。
```python
def make_great(magicians_name, modify_magicians_name):
    """伟大的魔术师"""
    while magicians_name:
        current_name = magicians_name.pop()

        modify_magicians_name.append('了不起的' + current_name)

def show_magicians(modify_magicians_name):
    """显示魔术师的名字"""
    print("\n下面出场的魔术师有：")
    for modify_magician_name in modify_magicians_name:
        print(modify_magician_name)

magicians_name = ['Eric', 'Alice', '刘谦']
modify_magicians_name = []

make_great(magicians_name, modify_magicians_name)
show_magicians(modify_magicians_name)
```
8-11 修改8-10的程序，在调用函数make_great()时，向它传递魔术师列表的副本。由于不想修改原始列表，请返回修改后的列表，并将其存储到另一个列表中。分贝使用这两个列表来调用show_magicians()，确认一个里列表包含的时原来的魔术师名字，而另一个包含的是添加了字样“the Great”的魔术师的名字。
```python
def make_great(magicians_name, modify_magicians_name):
    """伟大的魔术师"""
    while magicians_name:
        current_name = magicians_name.pop()

        modify_magicians_name.append('了不起的' + current_name)

def show_magicians(modify_magicians_name):
    """显示魔术师的名字"""
    print("\n下面出场的魔术师有：")
    for modify_magician_name in modify_magicians_name:
        print(modify_magician_name)

magicians_name = ['Eric', 'Alice', '刘谦']
modify_magicians_name = []

make_great(magicians_name[:], modify_magicians_name)
show_magicians(modify_magicians_name)
show_magicians(magicians_name)
```
8-12 编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点的三明治进行概述。调用这个函数三次，每次都提供不同数量的实参。
```python
def make_sandwichs(*toppings):
    """三明治的食材"""
    print("\n制作一个三明治，顾客需要以下食材：")
    for topping in toppings:
        print("-" + topping)

make_sandwichs('生菜', '沙拉')
make_sandwichs('洋葱', '牛排', '芝士')
make_sandwichs('鸡排', '番茄')
```
8-13 复制案例的程序user_profile.py，在其中调用build_profile()来创建有关你的简介；调用这个函数时，指定你的名和姓，以及三个描述你的键-值对。
```python
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('lance', 'wu',
                            location='shanghai',
                            job='logistics',
                            commute='bus')
print(user_profile)
```
8-14 编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接受制造商和型号，还接受任意数量的关键字实参。这样调用这个函数：提供必不可少的信息，以及两个名称-值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：

car = make_car('subaru', 'outback', color='blue', tow_package=True)

打印返回的字典，确认正确地处理了所有的信息。
```python
def make_cars(maker, type, **car_info):
    """包含了我们想知道汽车的一切信息"""
    car_files = {}
    car_files['maker_name'] = maker
    car_files['type_name'] = type
    for key, value in car_info.items():
        car_files[key] = value
    return car_files

car = make_cars('subaru', 'outback', color='blue', tow_package=True)
print(car)
```
