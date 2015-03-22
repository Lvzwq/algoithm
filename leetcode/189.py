class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.

    def rotate(self, nums, k):
        length = len(nums)
        if k == 0 or length == 0 or length == 1:
            pass
        else:
            j = k % length
            nums = [nums[(j + i) % length] for i in range(length)]
        print nums

    def rotate1(self, nums, k):
        length = len(nums)
        n = length - k % length
        for i in range(n):
            nums.append(nums[0])
            nums.pop(0)


s = Solution()
s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
s.rotate([-1], 2)
s.rotate([-1], 0)
s.rotate([1, 2], 1)
s.rotate([1, 2], 0)
