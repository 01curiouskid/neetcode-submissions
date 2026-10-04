class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        result=[]
        check=len(nums)/3
        for num, freq in count.items():
            if freq>check:
                result.append(num)
        return result