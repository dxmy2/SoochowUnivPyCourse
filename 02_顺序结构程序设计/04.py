# -*- coding:utf-8 -*-
# 作者：dxmy2
# 创建：2017-10-29
# 更新：2020-07-29
# 功能：编写一个程序显示当前北京时间，要求显示格式如下：当前时间是： 几时：几分：几秒

import datetime

# ===== main =====
if __name__ == "__main__":

    
    time = datetime .datetime.now()
    print(time)
    print(time.strftime('%H：%M：%S'))
