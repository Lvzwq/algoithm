class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.

    def rotate1(self, nums, k):
        length = len(nums)
        if k == 0 or k == 1:
            return
        if length == 1:
            return nums
        result = []
        j = k % length
        return [nums[(j + i) % length] for i in range(length)]

    def rotate(self, nums, k):
        length = len(nums)
        n = length - k % length
        for i in range(n):
            nums.append(nums[i])
        for i in range(n):
            nums.pop(0)

s = Solution()
s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
s.rotate([-1], 2)
s.rotate([-1], 0)
s.rotate([1, 2], 2)
s.rotate([1, 2], 0)
