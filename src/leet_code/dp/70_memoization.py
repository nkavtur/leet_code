class Solution:
    def climbStairs(self, n):
        memo = {1: 1, 2: 2, 3: 3}
        count = [0]

        self._climb_stairs_recursively(n, memo, count)
        return count[0]

    def _climb_stairs_recursively(self, n, memo, count):
        if n in memo:
            count[0] += memo[n]
            return

        if n >= 1:
            self._climb_stairs_recursively(n - 1, memo, count)
            memo[n - 1] = count[0]

        if n >= 2:
            self._climb_stairs_recursively(n - 2, memo, count)
            memo[n - 2] = count[0]


print(Solution().climbStairs(3))
print(Solution().climbStairs(4))
print(Solution().climbStairs(5))
print(Solution().climbStairs(6))
print(Solution().climbStairs(7))
print(Solution().climbStairs(8))
print(Solution().climbStairs(38))
