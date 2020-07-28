# -*- coding: utf-8 -*-
# 作者：dxmy2
# 创建：2017-10-29
# 更新：2020-07-23
# 功能：从键盘输入两个正整数  a  和  b  ，计算并输出  a/ b  的商和余数。

# ===== 参数说明 =====
# divisor：除数
# dividend：被除数
# remainder：余数
# quotient：商

# ===== 函数定义 =====
def getQuoAndRem(divisor,dividend):

    if (divisor <= 0) or (dividend <=0) :
        print("ParameterError:need positive integer!")
        return "error","error"
    else:
        if isinstance(divisor,int) and isinstance(dividend,int):

            quotient = dividend // divisor
            remainder = dividend % divisor

            return quotient,remainder
        else:
            print("ParameterError:need positive integer!")
            return "error","error"

    

# ===== 主函数 =====
if __name__ == "__main__":
    dividend,divisor = eval(input("Please input the dividend and divisor: "))
    quotient,remainder = getQuoAndRem(divisor,dividend)

    if quotient != "error":
        print("%d / %d = %d······%d" % (dividend,divisor,quotient,remainder))

