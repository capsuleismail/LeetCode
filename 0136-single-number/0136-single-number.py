class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            total = nums[i] ^ total
        return total