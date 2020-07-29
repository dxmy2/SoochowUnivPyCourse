# -*- coding:utf-8 -*-
# 作者：dxmy2
# 创建：2017-10-29
# 更新：2020-07-23
# 功能：产生一个随机3位正整数,并将该整数的数字首尾互换输出,例如：157互换后为751。

import random

# ====== 主函数 =====
if __name__ == "__main__":
    
    a=(random.randint(1,9))
    b=(random.randint(0,9))
    c=(random.randint(0,9))
    print (a*100+b*10+c)
    x=(c*100+b*10+a)
    print('%03d' % x)
