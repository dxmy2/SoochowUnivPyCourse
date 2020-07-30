# -*- coding:utf-8 -*-
# 作者：dxmy2
# 创建：2017-10-29
# 更新：2020-07-29
# 功能：随机产生一个[5,20]间的实数作为球的半径，求球的体积，输出半径和体积，7列，3位小数。

import random
import math
# ===== 参数说明 =====
# r: 球半径
# volume: 球体积

# ===== main =====
if __name__ =="__main__":

    r = random.uniform(5,20)
    volume = 4*math.pi*(r**3)/3

    print("%7.3f" %r)
    print("%7.3f" %volume)
