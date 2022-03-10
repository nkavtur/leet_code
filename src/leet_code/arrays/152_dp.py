class Solution:
    def maxProduct(self, nums):
        # find max_product for all contiguous subarrays not containing zeros
        indices = [-1] + [i for i, n in enumerate(nums) if n == 0] + [len(nums)]
        splits = [nums[i + 1:j] for i, j in zip(indices, indices[1:]) if len(nums[i + 1:j]) > 0]

        solutions = [self._max_product(s) for s in splits]
        if len(indices) > 2:
            solutions.append(0)

        return max(solutions)

    def _max_product(self, nums):
        if len(nums) == 1:
            return nums[0]

        result = max_p = min_p = nums[-1]
        for n in reversed(nums[:-1]):
            max_p, min_p = max(n, n * min_p, n * max_p), min(n, n * min_p, n * max_p)
            result = max(result, min_p, max_p)

        return result


# 3, 6, -30, -60, 120, 240, -960, -2880, -23040, 46080, 138240, -414720, -829440, (138240, -829440)
# 2, -10, -20, 40, 80, -320, -960, -7680, 15360, 46080, -138240, -276480, (46080, -276480)
# -5, -10, 20, 40, -160, -480, -3840, 7680, 23040, -69120, -138240, (23040, -138240)
# 2, -4, -8, 32, 96, 768, -1536, -4608, 13824, 27648, (-4608, 27648)
# -2, -4, 16, 48, 384, -768, -2304, 6912, 13824, (-2304, 13824)
# 2, -8, -24, -192, 384, 1152, -3456, -6912, (1152, -6912)
# -4, -12, -96, 192, 576, -1728, -3456, (576, -3456)
# 3, 24, -48, -144, 432, 864, (-144, 864)
# 8, -16, -48, 144, 288, (-48, 288)
# -2, -6, 18, 36, (-6, 36)
# 3, -9, -18,  (3, -18)
# -3, -6, (-3, -6)
# 2, (2, 2)

print(Solution().maxProduct([0]))

print(Solution().maxProduct([-2, 1, 0, -3]) == 1)
print(Solution().maxProduct([0, -3, 1, 1]) == 1)
print(Solution().maxProduct([2, 3, -2, 4]) == 6)
print(Solution().maxProduct([-2, 3, -4]) == 24)
print(Solution().maxProduct([-2, 0, -1]) == 0)
print(Solution().maxProduct([0, 2]) == 2)
print(Solution().maxProduct([3, -1, 4]) == 4)
print(Solution().maxProduct([-3, 0, 1, -2]) == 1)
print(Solution().maxProduct([2, -5, 2, -2, 2, -4, 3]) == 96)
print(Solution().maxProduct([3, 2, -5, 2, -2, 2, -4, 3, 8, -2, 3, -3, 2]) == 138240)
print(Solution().maxProduct([2, 3, -2, 0, 8]) == 8)
print(Solution().maxProduct([-3, 0, 1, -2]) == 1)
print(Solution().maxProduct([-3, -4, -7]) == 28)
print(Solution().maxProduct([-1, 1, 2, 1]) == 2)
