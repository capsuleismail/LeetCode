class Solution:
    def isHappy(self, number: int) -> bool:
        # 19 = 82
        # 82 = 68
        # 68 = 100
        # 100 = 1
        def squarenumber(number):
            result = 0
            while number:
                digit = number % 10
                digit = digit ** 2
                result += digit
                number //= 10
            return result
    
        checker = set()
    
        while number not in checker:
            checker.add(number)
            number = squarenumber(number)
            if number == 1:
                return True
        return False
            
            