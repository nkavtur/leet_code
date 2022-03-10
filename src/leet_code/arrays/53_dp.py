class Solution:
    def maxSubArray(self, nums):
        solution = nums.copy()

        for i in range(1, len(nums)):
            solution[i] = max(solution[i - 1] + nums[i], nums[i])

        return max(solution)


print(Solution().maxSubArray([-2, 1, -3, 4, -1, -1, 3, 1, -5, 4]))
print(Solution().maxSubArray([1, 2]))
print(Solution().maxSubArray([8, -19, 5, -4, 20]))
print(Solution().maxSubArray([-1, -1, -2, -2]))
