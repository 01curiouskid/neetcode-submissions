class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod=float('-inf')
        min_prod=float('inf')
        result=max_prod
        for num in nums:
            if num<0:
                max_prod, min_prod= min_prod, max_prod
            max_prod=max(num, num*max_prod)
            min_prod=min(num, num*min_prod)

            result = max(result,max_prod)
        return result