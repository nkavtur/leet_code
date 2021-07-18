class Solution:
    def longestPalindrome(self, s: str):
        if s == s[::-1]:
            return s

        longest = s[0]

        solution = [
            [False] * len(s)
            for _ in range(len(s))
        ]

        for i in range(len(s)):
            solution[i][i] = True
            if i + 1 < len(s) and s[i] == s[i + 1]:
                longest = s[i:i + 2]
                solution[i][i + 1] = True

        k = 3
        while k <= len(s):
            for i in range(len(s) - k + 1):
                start, end = i, i + k - 1
                if solution[start + 1][end - 1] and s[start] == s[end]:
                    longest = longest if len(longest) >= end - start + 1 else s[start:end + 1]
                    solution[start][end] = True
            k = k + 1

        return longest

