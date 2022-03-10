class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:

            if n & 1 == 1:
                result += 1

            n = n >> 1

        return result


print(Solution().hammingWeight(0b0000000000000000000000000001011))
print(Solution().hammingWeight(0b000000000000000000000010000000))
print(Solution().hammingWeight(0b11111111111111111111111111111101))
