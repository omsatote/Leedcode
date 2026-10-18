class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        import sys
        sys.setrecursionlimit(5000)
        MOD = 10**9 + 7
        n = len(nums)

        C = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            C[i][0] = 1
            for j in range(1, i + 1):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

        def ways(a):
            m = len(a)
            if m <= 2:
                return 1
            left = [x for x in a[1:] if x < a[0]]
            right = [x for x in a[1:] if x > a[0]]
            return C[m - 1][len(left)] * ways(left) % MOD * ways(right) % MOD

        return (ways(nums) - 1) % MOD