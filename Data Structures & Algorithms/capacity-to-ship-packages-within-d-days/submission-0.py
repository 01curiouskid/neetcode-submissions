class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high= max(weights), sum(weights)
        res=low
        while low<=high:
            mid = (low+high)//2
            day=0
            cap=mid
            for w in weights:
                if cap-w<0:
                    day+=1
                    cap=mid
                cap-=w
            day+=1
            if day<=days:
                high=mid-1
                res=mid
            else:
                low=mid+1
        return res