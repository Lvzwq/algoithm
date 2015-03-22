#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        length = len(s)
        if not length:
            return 0
        result = 1
        long_str = ''
        i = 0
        while i <= length - 1:
            flag = True
            temp_str = s[i]
            j = i + 1
            if result + i >= length or j > length - 1:
                return result
            # 优化
            if s[i:result + i] == long_str:
                temp_str = long_str
                j = i + result + 1
                i = i + result
            while flag:
                if s[j] in temp_str:
                    if len(temp_str) > result:
                        long_str = temp_str
                        result = len(temp_str)
                    flag = False
                else:
                    temp_str = temp_str + s[j]
                    if j >= length - 1:
                        if len(temp_str) > result:
                            long_str = temp_str
                            result = len(temp_str)
                        flag = False
                    j = j + 1
            i = i + 1
        return result


s = Solution()
print s.lengthOfLongestSubstring("ab")
print s.lengthOfLongestSubstring("abdeddcc")
#print s.lengthOfLongestSubstring("abcdefghijkalmanopqrstuvwxyzABddCDEFGHIJKLMNOPQRSTUVWXYZa0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ abcdefghijklmnopq")

