class Solution:
    def findMissingElements(self, nums):
        if not nums:
            return []

        s = set(nums)
        ans = []

        for x in range(min(s) + 1, max(s)):
            if x not in s:
                ans.append(x)

        return ans