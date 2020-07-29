# -*- coding：utf-8 -*-
# 作者：dxmy2
# 创建：2017-10-29
# 更新：2020-07-23
# 功能：编写程序让用户输入自己姓名，输出该姓名字符串的长度。

# ===== 参数说明 =====
# name：姓名
# nameLen：姓名长度

# ===== 函数定义 =====
def getNameLen():

    name = input("Please input your name: ")
    nameLen = len(name)

    print("Length of your name is %d" % nameLen)

# ===== 主函数 =====
if __name__ == "__main__":
    getNameLen()
