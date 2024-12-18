class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        
        while left <= right:
            middle = (left+right)//2
            m_squared = middle*middle
            
            if m_squared == x:
                return middle
            elif m_squared < x:
                left = middle + 1
            else:
                right = middle - 1
        return right
            
                
            