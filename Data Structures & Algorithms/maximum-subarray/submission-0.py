class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num=nums[0]
        curr_sum=0
        for num in nums:
            if curr_sum<0:
                curr_sum=0
            curr_sum+=num
            max_num=max(max_num,curr_sum)

        return max_num