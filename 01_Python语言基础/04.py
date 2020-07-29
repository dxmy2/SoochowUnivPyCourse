# -*- coding:utf-8 -*-
# 作者：dxmy2
# 创建：2017-10-29
# 更新：2020-07-23
# 功能：编写程序让用户输入两个平面上点的坐标，计算该两点间的距离

import math

# ===== 参数说明 =====
# piont1_X,piont1_Y：第一个点的坐标
# piont2_X,piont2_Y：第二个点的坐标
# distance：两点间距

# ===== 函数定义 =====
def getDistanceFromTwoPoints(piont1_X,piont1_Y,piont2_X,piont2_Y):
    
    distance = math.sqrt((piont1_X-piont2_X)**2+(piont1_Y-piont2_Y)**2)
    return distance

# ====== 主函数 =====
if __name__ == "__main__":
    piont1_X,piont1_Y = eval(input("Please input the first piont："))
    piont2_X,piont2_Y = eval(input("Please input the second piont："))
    distance = getDistanceFromTwoPoints(piont1_X,piont1_Y,piont2_X,piont2_Y)

    print("Distance between two points is %.2f" % distance)
