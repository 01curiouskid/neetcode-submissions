class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        
        def backtrack(idx, arr, nums):
            if idx==len(nums):
                res.append(arr.copy())
                return
            arr.append(nums[idx])
            backtrack(idx+1,arr,nums)
            arr.pop()
            while idx+1<len(nums) and nums[idx]==nums[idx+1]:
                idx+=1
            backtrack(idx+1,arr,nums)
        backtrack(0,[],nums)
        return res
        

         