class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left, right = 1, 1
        answer = [0] * len(nums)
        for i in range(len(nums)):
            answer[i] = left
            left *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        return answer