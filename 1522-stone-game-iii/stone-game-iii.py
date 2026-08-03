class Solution:
    def stoneGameIII(self, A):
        n = len(A)
        memo = {}

        def dfs(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]

            ans = -10**18
            total = 0

            for j in range(3):
                if i + j < n:
                    total += A[i + j]
                    ans = max(ans, total - dfs(i + j + 1))

            memo[i] = ans
            return ans

        diff = dfs(0)

        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        return "Tie"