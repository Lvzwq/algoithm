class Solution:
    # @param n, an integer
    # @return an integer

    def hammingWeight(self, n):
        i = 0
        while True:
            if n == 1:
                i = i + 1
                return i
            elif n % 2 == 0:
                n = n / 2
            else:
                i = i + 1
                n = n / 2

s = Solution()
print s.hammingWeight(121)
