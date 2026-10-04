class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results=[]
        def backtrack(idx,subset):
            if idx==len(nums):
                results.append(subset.copy())
                return
            backtrack(idx+1,subset)
            subset.append(nums[idx])
            backtrack(idx+1,subset)
            subset.pop()
        backtrack(0,[])
        return results

            
            