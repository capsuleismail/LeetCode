class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = ''
        while n:
            binary = str(n%2) + binary
            n//=2
            
        return binary.count('1')
        