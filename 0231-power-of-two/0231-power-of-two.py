class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        return (n&(n-1)) == 0
        
#2**(0) 0001
#2**(1) 0010
#2**(2)  0100
#2**(3)  1000
