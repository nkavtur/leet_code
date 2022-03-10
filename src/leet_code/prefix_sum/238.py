class Solution:
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)

        prefix, suffix = 1, 1
        for i in range(len(nums) - 1):
            prefix *= nums[i]
            suffix *= nums[-1 - i]

            answer[1 + i] *= prefix
            answer[-i - 2] *= suffix

        return answer


print(Solution().productExceptSelf([1, 2, 3, 4]))
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
