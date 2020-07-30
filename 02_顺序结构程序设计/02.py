# -*- coding:utf-8 -*-
# 作者：dxmy2
# 创建：2017-10-29
# 更新：2020-07-29
# 功能：用户输入三角形的三个顶点(x1,y1)、（x2,y2）、（x3,y3），
#       然后计算三角形面积，这里假定输入的三个点能构成三角形。
#       将面积输出到屏幕，要求占7列，保留2位小数，左对齐。

import math

# ===== 参数说明 =====
# x1,y1：第一个点的坐标，x2,y2，x3,y3 类似
# a,b,c: 三边长
# s: 周长/2，用于计算面积
# area：三角形的面积

# ===== main =====
if __name__ == "__main__":

    x1,y1 = eval(input("Please enter the first point coordinates:"))
    x2,y2 = eval(input("Please enter the second point coordinates:"))
    x3,y3 = eval(input("Please enter the third point coordinates:"))

    a=math.sqrt((x1-x2)**2+(y1-y2)**2)
    b=math.sqrt((x1-x3)**2+(y1-y3)**2)
    c=math.sqrt((x2-x3)**2+(y2-y3)**2)

    s = (a+b+c)/2

    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print("The area of the triangle is %7.2f" %area)
