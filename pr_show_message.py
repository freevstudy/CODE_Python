# 创建一个包含简短文本的列表
messages = [
    "会议改到下午3点。",
    "提醒：今天提交周报。",
    "中午12点食堂聚餐。",
    "系统将于18:00升级维护。",
    "请查收最新项目文档。",
]

sent_messages = []


def show_messages(message_list):
    """展示消息列表"""
    print("\n====== 消息内容展示 ======")
    for msg in message_list:
        print(f"* {msg}")
    print("============================")


def send_messages(src_list, dst_list):
    """
    消息发送函数
    :param src_list: 原始消息列表(会被清空)
    :param dst_list: 已发送消息列表(会被填充)
    """
    print("\n====== 开始发送消息 ======")
    while src_list:
        current_msg = src_list.pop(0)  # 从原列表移除第一条消息
        print(f"正在发送：{current_msg}")
        dst_list.append(current_msg)  # 添加已发送列表
    print("所有消息发送完成！")


# 展示原始消息列表
print("原始消息列表：")
show_messages(messages)

# 执行消息发送
send_messages(messages, sent_messages)

# 验证结果
print("\n发送后验证：")
print("原始消息列表长度：", len(messages))
print("已发送消息列表长度：", len(sent_messages))

print("\n原始消息内容：")
show_messages(messages)

print("\n已发送消息内容：")
show_messages(sent_messages)
