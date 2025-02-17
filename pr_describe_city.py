# 编辑一个有关城市信息的函数，所属国家做为形参的默认值
def describe_city(city_name, city_nation = '中国'):
    """有关城市所属的国家"""
    print(f"{city_name}所属的国家是{city_nation}。")

describe_city('北京')
describe_city('上海')
describe_city('东京', '日本')

