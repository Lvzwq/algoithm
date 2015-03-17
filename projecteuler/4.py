#!/bin/python env

dis = 1000
def is_palindromic(num):
    li = str(num)
    i = 0
    length = len(li)
    while(i <length/2):
        if li[i] == li[length-i-1]:
            i = i + 1
        else:
            return False
    return True

def get_max_p(num):
    n = 2
    while(1):
        i = n/2
        while(i >= 1):
            a = num - i
            b = num + i - n
            result = a * b
            if is_palindromic(result):
                return result, a, b
            else:
                i = i - 1
        n = n + 1


print get_max_p(1000)
print is_palindromic(998001)
