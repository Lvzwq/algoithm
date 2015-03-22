#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @return an integer
    def reverse(self, x):
        if x == 0:
            return 0
        elif x > 0:
            str_x = str(x)
        else:
            str_x = str(x * (-1))
        length = len(str_x)
        x_list = []
        for i in range(length):
            if str_x[length - 1 - i] == '0' and not x_list:
                pass
            else:
                x_list.append(str_x[length - 1 - i])
        # x_list = [str_x[length-i-1] for i in range(length) if str_x[length-i-1] != '0' and ]
        result = ''
        for i in x_list:
            result = result + i
        result = int(result)
        if result >= 2147483648:
            return 0
        if x <= 0:
            result = result * (-1)
        return result


s = Solution()
print s.reverse(-123)


