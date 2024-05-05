class Solution:
    def addBinary(self, a: str, b: str) -> str:
        first = int(a, 2)
        second = int(b, 2)
        result = first + second
        return '{0:b}'.format(result)