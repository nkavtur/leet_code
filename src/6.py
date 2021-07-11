class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = numRows + numRows - 2
        rows = [[] for _ in range(numRows)]

        for i in range(len(s)):
            reminder = i % n
            if 0 <= reminder <= numRows - 1:
                rows[reminder].append(s[i])
            else:
                rows[n - reminder].append(s[i])

        return "".join(["".join(row) for row in rows])
