class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                elif text1[i] != text2[j]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        res = 0
        for i in range(len(text1)):
            for j in range(len(text2)):
                res = max(res, dp[i][j])

        return res


print(Solution().longestCommonSubsequence('aced', 'cead') == 3)
print(Solution().longestCommonSubsequence('abcde', 'ace') == 3)
print(Solution().longestCommonSubsequence('abc', 'abc') == 3)
print(Solution().longestCommonSubsequence('abc', 'def') == 0)
print(Solution().longestCommonSubsequence('abcba', 'abcbcba') == 5)
print(Solution().longestCommonSubsequence("yqpq", "yqp") == 3)
print(Solution().longestCommonSubsequence("yqpq", "yaqp") == 3)
# #
print(Solution().longestCommonSubsequence("bbm", "mbbk") == 2)
print(Solution().longestCommonSubsequence("bbm", "mbk") == 1)
print(Solution().longestCommonSubsequence('cvqciqxzaz', 'ccvqiqzaz') == 8)

# m b k    b b m
#              1

# a = [1, 2, 3, 4]

text1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
text2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(Solution().longestCommonSubsequence(text1, text2) == 210)
