class Solution:
    # @param n, an integer
    # @return an integer

    def reverseBits(self, n):
        result = []
        re = 0
        while True:
            if n == 0:
                for i in range(len(result)):
                    if result[i] == 1:
                        re = re + 2 ** (31 - i)
                return re
            while n % 2 == 0:
                result.append(0)
                n = n / 2

            if n % 2 == 1:
                result.append(1)
                n = n / 2

s = Solution()
print s.reverseBits(43261596)
