class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Two pointers, left from start, right from end
        left = 0
        right = len(s) - 1

        # 2. Keep going until two hands meet
        while left < right:
            # 3. Left hand: skip non-letter/number
            while left < right and not s[left].isalnum():
                left += 1
            # 4. Right hand: skip non-letter/number
            while left < right and not s[right].isalnum():
                right -= 1
            # 5. Compare: both lowercase, not equal → False
            if s[left].lower() != s[right].lower():
                return False
            # 6. This pair matched, move both hands inward
            left += 1
            right -= 1
        # 7. All pairs matched → True
        return True