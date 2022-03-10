class Solution:
    def threeSum(self, nums):
        sorted_nums = sorted(nums)

        triplets = []
        for i in range(len(sorted_nums) - 1):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            self._two_sum(i, sorted_nums, triplets)

        return triplets

    def _two_sum(self, first_val_index, sorted_nums, triplets):
        low, high = first_val_index + 1, len(sorted_nums) - 1

        first_value = sorted_nums[first_val_index]
        while low != high:

            if sorted_nums[low] + sorted_nums[high] + first_value > 0:
                high -= 1
            elif sorted_nums[low] + sorted_nums[high] + first_value < 0:
                low += 1
            else:
                triplets.append((first_value, sorted_nums[low], sorted_nums[high]))
                low += 1


# print(Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]))
# print(Solution().threeSum(nums=[]))
print(Solution().threeSum(nums=[-2, 0, 1, 1, 2]))
