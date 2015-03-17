#!/bin/python env

n = 100
result1 = sum((i*i for i in range(1,n+1)))
num = sum(range(1,n+1))
result2 = num * num
print result2 - result1
