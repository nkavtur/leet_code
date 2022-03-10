class Solution:
    def maxSubArray(self, nums):
        max_sum, current_sum = nums[0], 0

        for n in nums:
            if n >= current_sum and current_sum <= 0:
                current_sum = n
            else:
                current_sum += n
            max_sum = max(max_sum, current_sum)

        return max_sum


print(Solution().maxSubArray([-2, 1, -3, 4, -1, -1, 3, 1, -5, 4]))
print(Solution().maxSubArray([1, 2]))
print(Solution().maxSubArray([8, -19, 5, -4, 20]))
print(Solution().maxSubArray([-1, -1, -2, -2]))
