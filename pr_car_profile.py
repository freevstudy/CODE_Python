def make_car(maker, model, **car_info):
    """有关我们所知有关一辆汽车的信息"""
    car_info["制造商"] = maker
    car_info["汽车型号"] = model
    return car_info


car_profile = make_car("比亚迪", "比亚迪海鸥", color="暖阳白", two_packge=True)
print("汽车型号：", car_profile)
