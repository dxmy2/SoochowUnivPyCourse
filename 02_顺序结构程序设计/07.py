# -*- coding:utf-8 -*-
# 作者：dxmy2
# 创建：2017-10-29
# 更新：2020-07-29
# 功能：计算当前距离1970年1月1日过去了多少天又多少小时，并输出到屏幕上

import time

# ===== 参数说明 =====
# seconds：距1970.1.1的秒数
# days：距1970.1.1的天数
# hours：距1970.1.1的小时数

# ===== main =====
if __name__ == "__main__":

    seconds = round(time.time())
    days = seconds // (24*60*60)
    hours = (seconds % (24*60*60) ) /3600 + 8

    print("%d days and %.2f hours have passed since January 1, 1970." %(days,hours))
