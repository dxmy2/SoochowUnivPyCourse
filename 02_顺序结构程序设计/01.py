# -*- coding:utf-8 -*-
# 作者：dxmy2
# 创建：2017-10-29
# 更新：2020-07-29
# 功能：从键盘输入一个3位整数，请编写程序计算三位整数的各位数字之和，
#       并输出到屏幕上，要求输出占4列，右对齐。

# ===== 参数说明 =====
# divNum：输入的3位数
# hundred：百位数字
# ten：十位数
# one：个位数
# sumNum：各位数字之和

# ===== 主函数 =====
if __name__ == "__main__":

    # 不考虑输入错误
    divNum = int(input("Please enter a three-digit integer："))
    
    hundred = divNum // 100
    ten = (divNum // 10) % 10
    one = (divNum % 100) % 10

    sumNum = one + ten + hundred
    
    print("The sum of the digits of a three-digit integer:%4d" %sumNum)
