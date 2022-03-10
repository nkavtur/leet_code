class Solution:
    def climbStairs(self, n):
        dp = [0, 1, 2, 3]

        for i in range(4, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[n]


print(Solution().climbStairs(3))
print(Solution().climbStairs(4))
print(Solution().climbStairs(5))
print(Solution().climbStairs(38))
