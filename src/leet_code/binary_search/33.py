class Solution:
    def search(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[low] == target:
                return low

            if nums[high] == target:
                return high

            # [..., 7, 8, 9, 0, 1, 2], target = 0 or 1
            if nums[mid] > nums[high] > target:
                low = mid + 1

            # [..., 7, 8, 9, 0, 1, 2], target = 8 or 9
            elif nums[high] < nums[mid] < target:
                low = mid + 1

            # [..., 7, 8, 9, 10, 11, 12], target = 8 or 9 or 10 or 11
            elif nums[mid] < nums[high] and nums[mid] < target < nums[high]:
                low = mid + 1

            # target in the left half
            else:
                high = mid - 1

        return -1


# print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
# print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
# print(Solution().search(nums=[1], target=0))
# print(Solution().search([1, 2, 3, 4, 5, 6], 4))
# print(Solution().search([5, 1, 2, 3, 4], 1))
