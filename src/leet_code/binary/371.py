class Solution:
    def getSum(self, a, b):
        mask = 0b11111111
        while b & mask:
            carry = a & b
            a = a ^ b
            b = carry << 1

        return (a & mask) if b > mask else a


print(Solution().getSum(-1, 1))
