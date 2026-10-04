class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:  
        self.res=[]
        self.backtrack([], nums, [False]*len(nums))
        return self.res
    def backtrack(self,perm,nums,picks):
        if len(perm)==len(nums):
            self.res.append(perm.copy())
            return
        for i in range(len(nums)):
            if not picks[i]:
                perm.append(nums[i])
                picks[i]=True
                self.backtrack(perm,nums,picks)
                perm.pop()
                picks[i]=False
        
        