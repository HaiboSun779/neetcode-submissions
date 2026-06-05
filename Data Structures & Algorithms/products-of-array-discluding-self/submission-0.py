class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        perfix = 1
        for i in range(n):
            result[i] = perfix
            perfix *= nums[i]
        
        suffix = 1
        for i in range(n -1 , -1 , -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result