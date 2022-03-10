class Solution:

    def __init__(self):
        self.memo = dict()

    def coinChange(self, coins, amount):
        self.coin_change_recursively(coins, amount)
        return self.memo[amount]

    def coin_change_recursively(self, coins, amount):
        if amount < 0:
            return -1

        if amount == 0:
            return 0

        if amount in self.memo:
            return self.memo[amount]

        _min = float("+infinity")
        for coin in coins:
            res = self.coin_change_recursively(coins, amount - coin)
            if 0 <= res < _min:
                _min = res + 1

        self.memo[amount] = _min if _min != float("+infinity") else -1
        return self.memo[amount]


# print(Solution().coinChange(coins=[1, 2, 5], amount=11))
# print(Solution().coinChange(coins=[2], amount=3))
# print(Solution().coinChange(coins=[2147483647], amount=2))
# print(Solution().coinChange(coins=[1], amount=0))
# print(Solution().coinChange(coins=[1, 2147483647], amount=2))
# print(Solution().coinChange(coins=[1, 3, 5], amount=1))
print(Solution().coinChange([186, 419, 83, 408], 6249))
# print(Solution().coinChange(coins=[2, 3, 6, 7], amount=11))
# print(Solution().coinChange([4, 6], 20))
