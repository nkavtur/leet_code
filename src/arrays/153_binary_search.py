class Solution:
    def findMin(self, nums):
        result = float("+infinity")

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            # Given we are at nums[mid] position.
            # On the left we see: [nums[low], nums[low+1], ..., nums[mid-2], nums[mid-1]],
            # on the right: [nums[mid+1], nums[mid+2], ..., nums[high-1], nums[high]].

            head = nums[low]
            left_neighbour = nums[max(mid - 1, 0)]
            min_left = min(head, left_neighbour)

            tail = nums[high]
            right_neighbour = nums[min(mid + 1, len(nums) - 1)]
            min_right = min(tail, right_neighbour)

            result = min(min_left, min_right, result)

            if min_left < min_right:
                high = mid - 1
            else:
                low = mid + 1

        return result


print(Solution().findMin([3, 4, 5, 1, 2]) == 1)
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0)
print(Solution().findMin([11, 13, 15, 17]) == 11)
print(Solution().findMin([5, 1, 2, 3, 4]) == 1)
print(Solution().findMin([2, 3, 4, 5, 1]) == 1)
print(Solution().findMin([3, 4, 5, 6, 1, 2]) == 1)
