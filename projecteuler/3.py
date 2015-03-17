#!/bin/python env
import math
def max_zhiyinshu(num):
    n = 3
    num = get_num(2,num)
    num = get_num(3,num)
    num = get_num(5,num)
    num = get_num(7,num)
    while(n <= math.sqrt(num)):
        if num % n == 0:
            num = get_num(n,num)
        n = n + 2
        if n % 3 ==0 or n % 5 ==0 or n % 7 == 0:
            n = n + 2
    return num

def get_num(n, num):
    while(num % n == 0):
        num = num/n
    return num
print max_zhiyinshu(13195)
print max_zhiyinshu(600851475143)          
        
