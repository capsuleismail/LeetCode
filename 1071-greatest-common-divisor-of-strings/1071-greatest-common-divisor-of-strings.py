class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        length_1 = len(str1) 
        length_2 = len(str2)
        
        def isDivisor(l):
            if length_1 % l or length_2 % l: 
                return False
            #factors
            f1, f2 = (length_1 // l), (length_2 // l)
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(length_1, length_2), 0, -1):
            if isDivisor(l):
                return str1[:l]
        return ""
        