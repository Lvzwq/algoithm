#!/bin/python env
# -*-coding: utf-8 -*-
prime_num = [2,3]

num = 10001

def get_prime(num):
    n = 2
    result = 3
    while(1):
        if is_prime(prime_num, result):
            prime_num.append(result)
            n = n + 1
            if n == num:
                return result
        result = result + 2


# 判断是否是质数
def is_prime(prime_num, result):
    for i in prime_num:
        if result % i == 0:
            return False
        else:
            pass
    return True
print get_prime(num)
