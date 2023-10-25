class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        start = 0
        max_length = 0
        for i in range(len(s)):
            palindrome1 = expand_around_center(i, i)
            if len(palindrome1) > max_length:
                max_length = len(palindrome1)
                start = i - len(palindrome1) // 2
            palindrome2 = expand_around_center(i, i + 1)
            if len(palindrome2) > max_length:
                max_length = len(palindrome2)
                start = i - len(palindrome2) // 2 + 1
        return s[start:start + max_length]
        