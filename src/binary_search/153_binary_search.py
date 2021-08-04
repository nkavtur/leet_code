class Solution:
    def findMin(self, nums):
        result = float("+infinity")

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            result = min(nums[mid], result)

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1

        return result


print(Solution().findMin([3, 4, 5, 1, 2]) == 1)
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0)
print(Solution().findMin([11, 13, 15, 17]) == 11)
print(Solution().findMin([5, 1, 2, 3, 4]) == 1)
print(Solution().findMin([2, 3, 4, 5, 1]) == 1)
print(Solution().findMin([3, 4, 5, 6, 1, 2]) == 1)
