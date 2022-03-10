class Solution:
    def findMin(self, nums):
        return self._findMin_recursively(nums)

    def _findMin_recursively(self, nums):
        if len(nums) == 1:
            return nums[0]

        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        return min(self._findMin_recursively(left), self._findMin_recursively(right))


print(Solution().findMin([3, 4, 5, 1, 2]) == 1)
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0)
print(Solution().findMin([11, 13, 15, 17]) == 11)
print(Solution().findMin([5, 1, 2, 3, 4]) == 1)
print(Solution().findMin([2, 3, 4, 5, 1]) == 1)
print(Solution().findMin([3, 4, 5, 6, 1, 2]) == 1)
