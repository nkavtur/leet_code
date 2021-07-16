class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for n in nums:
            if n in seen or seen.add(n):
                return True

        return False
