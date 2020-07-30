# -*- coding:utf-8 -*-
# 作者：dxmy2
# 创建：2017-10-29
# 更新：2020-07-29
# 功能：产生随机复数，计算复数的模和辐角

import random
import math

# ===== 参数说明 =====
# real：复数的实部
# imag：复数的虚部
# com：复数
# mod：模
# arg：辐角

# ===== main =====
if __name__ =="__main__":
    
    real=random.randrange(10,50)
    imag=random.randrange(10,50)
    com=complex(real,imag)

    mod = math.sqrt(real**2+imag**2)
    arg = math.atan(imag/real) * 180 / math.pi
    print('%7s,%7.2f,%7.2f°' %(com,mod,arg))
