# 用函数创建一个描述音乐专辑的字典，包含歌手名字和专辑名；其中至少一个字典要有专辑的歌曲数量
def get_album(singer_album, name_album, singnum=None):
    """返回一个专辑的信息"""
    album = {"singer": singer_album, "name": name_album}
    if singnum:
        album["singnum"] = singnum
    return album


message = get_album("周杰伦", "叶惠美")
print(message)

message = get_album("邓紫棋", "新的心跳")
print(message)

message = get_album("刀郎", "山河寥哉", singnum=22)
print(message)
