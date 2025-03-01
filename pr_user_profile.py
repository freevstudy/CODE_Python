def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切。"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


# 创建第一个用户档案
user_profile1 = build_profile(
    "albert", "einstein", location="princeton", field="physics"
)
# 创建第二个用户档案
user_profile2 = build_profile(
    "Lance", "Wu", location="Shanghai", field="logistics", post="store cherk"
)

# 输出两个用户档案
print("爱因斯坦的档案：", user_profile1)
print("吴先生的档案：", user_profile2)
