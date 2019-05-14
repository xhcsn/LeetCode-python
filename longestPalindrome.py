class Solution:
    def is_huiwen(self, s):
        i = 0
        while i < len(s) // 2:
            if s[i] == s[len(s) - 1 - i]:
                i += 1
            else:
                return False
        return True

    def longestPalindrome(self, s: str) -> str:
        huiwen = []
        if len(s) == 1:
            return s
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if is_huiwen(s[i:j]):
                    huiwen.append(s[i:j])
        return huiwen