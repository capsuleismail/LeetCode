class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0 
        for letter in s:
            result = result ^ ord(letter)
        for letter in t:
             result = result ^ ord(letter)
        return chr(result)