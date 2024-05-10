class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''
        for i in range(len(s)):
            if s[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijlkmnopqrstuvwxyz0123456789':
                result += s[i].lower()
        return result[::-1] == result