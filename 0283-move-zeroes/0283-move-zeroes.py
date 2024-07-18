class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        not_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[not_zero] = nums[i]
                not_zero += 1
        for i in range(not_zero, len(nums)):
            nums[i] = 0
        return nums
            
    
    
