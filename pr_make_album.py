# 用while循环，让用户输入专辑和歌手，while循环要有退出机制
def make_album(singer_album, name_album):
    """返回一个专辑的信息"""
    album = {"singer": singer_album, "name": name_album}
    return album


while True:
    print("\n请输入专辑的相关信息：")
    print("（当输入'q'时会退出输入界面。）")

    s_album = input("专辑歌手：")
    if s_album == "q":
        break

    n_album = input("专辑名称：")
    if n_album == "q":
        break

    albm_info = make_album(s_album, n_album)
    print(f"您输入的专辑信息是：\n{albm_info}")
