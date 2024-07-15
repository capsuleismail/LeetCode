class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        i = n - 1
    
        while k > 0 and i >= 0:
            num[i] += k
        

            k = num[i] // 10
            num[i] %= 10

            i -= 1

        while k > 0:
            num.insert(0, k % 10)
            k //= 10
    
        return num