class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]

        return self._find_recursively(nums)

    def _find_recursively(self, nums):
        if len(nums) <= 2:
            return max(sum(nums), max(nums))

        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        left_sum = self._find_recursively(left)
        right_sum = self._find_recursively(right)
        cross_sum = self._cross_solution(left, right)

        return max(left_sum, right_sum, cross_sum)

    def _cross_solution(self, left, right):
        # left_sum
        max_left_sum = left_sum = right[0]
        for i in range(len(left) - 1, -1, -1):
            left_sum = left_sum + left[i]
            max_left_sum = max(left_sum, max_left_sum)

        # right sum
        max_right_sum = right[1]
        right_sum = 0
        for i in range(1, len(right)):
            right_sum = right_sum + right[i]
            max_right_sum = max(right_sum, max_right_sum)

        return max(max_left_sum + max_right_sum, max_left_sum, max_right_sum)


print(Solution().maxSubArray([-2, 1, -3, 4, -1, -1, 3, 1, -5]))
print(Solution().maxSubArray([1, 2]))
print(Solution().maxSubArray([8, -19, 5, -4, 20]))
print(Solution().maxSubArray([-1, -1, -2, -2]))
