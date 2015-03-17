#!/bin/python env
def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibo(n-1) + fibo(n-2)

fnum = [1,2]
n = 2
while(1):
    n = n + 1
    fn= fibo(n)
    if fn > 4000000:
        break;
    else:
        fnum.append(fn)
#print fnum
result = sum([ fnum[i] for i in range(len(fnum)) if i % 3 == 1])
print result
