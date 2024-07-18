class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
                
        result = []
        for num in nums:
            if num != 0:
                result.append(num)

   
        zero_count = length - len(result)
        result.extend([0] * zero_count)

        return result
