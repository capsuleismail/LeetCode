class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n <= 0:
            return False
    
        primers = [2, 3, 5]
    
        for value in primers:
            while n % value == 0:
                n = n // value
            
            
        return n == 1
