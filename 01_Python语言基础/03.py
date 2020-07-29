# -*- coding:utf-8 -*-
# 作者：dxmy2
# 创建：2017-10-29
# 更新：2020-07-23
# 功能：一只大象口渴了，要喝 20 升水才能解渴，但现在只有一个深 h 厘米，底面半径为 r 厘米的小圆桶(h 和 r 都是整数)。
#       问大象至少要喝多少桶水才会解渴。
#       编写程序输入半径和高度，输出需要的桶数（一定是整数）。

import math

# ===== 参数说明 =====
# h：圆桶高度(cm)
# r：圆桶底面半径(cm)
# volum：圆桶体积(cm²)
# buckeNum：圆桶数量

# ===== 函数定义 =====
def getVolume(r,h):

    if ( r <=0 ) or ( h <= 0 ):
        print("ParameterError:need positive integer!")
        return "error"
    else:
        if isinstance(r,int) and isinstance(h,int):

            volume = math.pi * r * r * h

            return volume
        else:
            print("ParameterError:need positive integer!")
            return "error"

# ===== 主函数 =====
if __name__ == "__main__":
    r,h = eval(input("Please input the r,h of the bucket :"))
    volume = getVolume(r,h)
    if volume != "error":
        bucketNum = 2000 // volume + 1

        print("The elephant has to drink at least %d buckets of water to quench it's thirst." % bucketNum)
