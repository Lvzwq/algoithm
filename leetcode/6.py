#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def convert(self, s, nRows):
        if nRows <= 1:
            return s
        if len(s) <= 2 or len(s) <= nRows:
            return s
        result = ''
        for i in range(nRows):
            j = i
            flag = True
            while True:
                try:
                    result = result + s[j]
                except IndexError:
                    break
                else:
                    if i == nRows - 1:
                        j = j + 2 * nRows - 2
                        continue
                    if flag:
                        j = j + nRows * 2 - 2 - i * 2
                        flag = False
                    else:
                        j = j + 2 * i
                        flag = True
        return result


s = Solution()
print s.convert('ABCD', 3)
