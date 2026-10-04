class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)/2
        if not target.is_integer():
            return False
        dp=set()
        dp.add(0)

        for i in range(len(nums)-1,-1,-1):
             for t in dp.copy():
                dp.add(t+nums[i])
                if target in dp:
                    return True
        return False