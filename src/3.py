from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        frequency = defaultdict(int)
        max_length, current_length = 0, 0
        window_start, window_end = 0, 0

        for window_end in range(len(s)):
            frequency[s[window_end]] += 1

            current_length = window_end - window_start + 1
            if frequency[s[window_end]] == 1:
                max_length = max(max_length, current_length)

            while frequency[s[window_end]] > 1:
                frequency[s[window_start]] -= 1
                window_start += 1

        return max_length
