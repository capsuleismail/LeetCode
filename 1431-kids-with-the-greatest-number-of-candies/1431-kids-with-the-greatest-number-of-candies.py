class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        return map(lambda x: x+extraCandies>=maximum, candies)
        