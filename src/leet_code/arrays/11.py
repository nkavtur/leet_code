class Solution:
    def maxArea(self, heights):
        if len(heights) == 2:
            return min(heights[0], heights[1])

        max_area = 0
        low, high = 0, len(heights) - 1

        while low < high:
            max_area = max(max_area, (high - low) * min(heights[high], heights[low]))

            if heights[low] < heights[high]:
                low += 1
            else:
                high -= 1

        return max_area


print(Solution().maxArea(heights=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
# print(Solution().maxArea(heights=[1, 1]))
# print(Solution().maxArea(heights=[4, 3, 2, 1, 4]))
# print(Solution().maxArea(heights=[1, 2, 1]))
# print(Solution().maxArea(heights=[1, 2]))
# print(Solution().maxArea(heights=[1, 2, 4, 3]))
# print(Solution().maxArea([1, 3, 2, 5, 25, 24, 5]))

#        |
#      | |
#   |  | |
# | |  | |
