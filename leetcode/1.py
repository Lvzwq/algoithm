#!/bin/python env
# -*-coding:utf-8 -*-


class Solution:
    # @return a tuple, (index1, index2)
    # flag = True

    def twoSum(self, num, target):
        length = len(num)
        i = 0
        j = length - 1
        sort_num = sorted(num)
        if sort_num[i] + sort_num[j] == target:
            return (num.index(sort_num[i]) + 1, num.index(sort_num[j]) + 1)
        elif sort_num[i] + sort_num[j] > target:
            flag = True
        else:
            flag = False
        while j > i:
            if sort_num[i] + sort_num[j] == target:  # 得到target的两个数相同
                a = num.index(sort_num[i])
                if sort_num[i]  == sort_num[j]:
                    for k in range(length):
                        if num[length - k -1] == num[a]:
                            return (a + 1, length - k)
                        else:
                            pass
                else:
                    b = num.index(sort_num[j])
                    if a > b:
                        return (b + 1, a + 1)
                    else:
                        return (a + 1, b + 1)
            elif sort_num[i] + sort_num[j] > target:
                flag = True
            else:
                flag = False
            if flag:
                j = j - 1
            else:
                i = i + 1
s = Solution()
print s.twoSum([-1, -2, -3, -4, -5], -7)
print s.twoSum([2, 4, 5, 6, 7, 8, 10, 43, 49, 55], 50)
print s.twoSum([0, 3, 2, 0], 0)
