class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=len(nums)//2
        count=Counter(nums)
        for key, val in count.items():
            if val>maj:
                return key
