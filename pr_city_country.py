# 编写接受城市名称及其所属国家的函数，并且返回
def city_country(city_name, country_name):
    """返回城市名称及其所属国家"""
    countryofcity = f"{city_name},{country_name}"
    return countryofcity.title()


message = city_country("上海", "中国")
print(message)

message = city_country("纽约", "美国")
print(message)

message = city_country("雅典", "希腊")
print(message)
