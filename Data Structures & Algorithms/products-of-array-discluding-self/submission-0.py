class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length
        for i in range(1, length):
            output[i] = output[i-1] *nums[i-1]
        pred=1
        for i in range(length-2,-1,-1):
            pred *= nums[i+1]
            output[i] *= pred
        return output


