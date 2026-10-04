class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map={0:1}
        res=0
        curSum=0
        for n in nums:
            curSum+=n
            diff=curSum-k
            res += prefix_map.get(diff,0)
            prefix_map[curSum]=1+prefix_map.get(curSum,0)
        return res