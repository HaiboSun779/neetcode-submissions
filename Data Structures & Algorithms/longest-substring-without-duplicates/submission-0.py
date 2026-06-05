class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_len = 0

        for right, c in enumerate(s):
            while c in seen:
                seen.remove(s[left])
                left += 1
            seen.add(c)
            max_len = max(max_len, right - left + 1)
        return max_len