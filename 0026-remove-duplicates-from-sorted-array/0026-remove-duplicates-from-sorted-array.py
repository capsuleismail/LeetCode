class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for index in range(1, len(nums)):
            if nums[index] != nums[index-1]:
                nums[left] = nums[index]
                left += 1
        return left
 