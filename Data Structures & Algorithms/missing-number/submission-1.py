class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        res=n #becaz loop is not going till n
        for i in range(n):
            res = res^i^nums[i]
        return res