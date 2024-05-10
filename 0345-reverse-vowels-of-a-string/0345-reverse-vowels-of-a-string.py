class Solution:
    def reverseVowels(self, s: str) -> str:
        result = ''
        string = list(s)
        left, right = 0, len(string)-1
        while left<right:
            while left < right and string[left] not in 'AEIOUaeiou':
                left += 1
            while left < right and string[right] not in 'AEIOUaeiou':
                right -= 1
            if left < right:
                string[left], string[right] = string[right], string[left]
                left += 1
                right -= 1
        return ''.join(string)