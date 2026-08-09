from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # Initialize the memoization table
        n = len(piles)
        memo = [[0] * (n + 1) for _ in range(n)]

        # Initialize the suffix sum array
        suffix_sum = piles[:]

        # Compute suffix sums
        for i in range(n - 2, -1, -1):
            suffix_sum[i] += suffix_sum[i + 1]

        # Return the maximum stones Alex can collect
        return self.max_stones(suffix_sum, 1, 0, memo)

    def max_stones(
        self,
        suffix_sum: List[int],
        max_till_now: int,
        curr_index: int,
        memo: List[List[int]],
    ) -> int:

        # If Alex can take all remaining piles
        if curr_index + 2 * max_till_now >= len(suffix_sum):
            return suffix_sum[curr_index]

        # Return memoized answer
        if memo[curr_index][max_till_now] != 0:
            return memo[curr_index][max_till_now]

        # Opponent's minimum possible score
        res = float("inf")

        for x in range(1, 2 * max_till_now + 1):
            res = min(
                res,
                self.max_stones(
                    suffix_sum,
                    max(max_till_now, x),
                    curr_index + x,
                    memo,
                ),
            )

        # Current player's score
        memo[curr_index][max_till_now] = suffix_sum[curr_index] - res
        return memo[curr_index][max_till_now]