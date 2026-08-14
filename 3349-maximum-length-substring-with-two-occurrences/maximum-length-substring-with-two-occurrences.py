class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = [0] * 26
        left = 0
        max_len = 0

        for right in range(len(s)):
            count[ord(s[right]) - ord('a')] += 1

            while count[ord(s[right]) - ord('a')] > 2:
                count[ord(s[left]) - ord('a')] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len