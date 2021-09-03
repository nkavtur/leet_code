class Solution:
    def coinChange(self, coins, amount):
        dp = [float("+infinity")] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != float("+infinity") else -1


# print(Solution().coinChange(coins=[1, 2, 5], amount=11))
# print(Solution().coinChange(coins=[2], amount=3))
# print(Solution().coinChange(coins=[2147483647], amount=2))
# print(Solution().coinChange(coins=[1], amount=0))
# print(Solution().coinChange(coins=[1, 2147483647], amount=2))
# print(Solution().coinChange(coins=[1, 3, 5], amount=1))
print(Solution().coinChange([186, 419, 83, 408], 6249))
# print(Solution().coinChange(coins=[2, 3, 6, 7], amount=11))
# print(Solution().coinChange([4, 6], 20))
