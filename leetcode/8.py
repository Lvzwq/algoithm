class Solution:
    # @return an integer

    def atoi(self, str):
        result = ''
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if not str:
            return 0
        for i in range(len(str)):
            if str[i] == ' ':
                continue
            elif str[i] in num:
                result = result + str[i]
            elif str[i] in ['+', '-']:
                if len(result) == 0:
                    result = result + str[i]
                else:
                    break
        if result == '+' or result == '-':
            return 0
        return int(result)


s = Solution()
print s.atoi('    -123')
