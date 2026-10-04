class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxP=max(piles)
        
        low,high=1,maxP
        while low<=high:
            middle=(low+high)//2
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/middle)
            # print(hours)
            if low==high:
                return low
            elif hours<=h:
                high=middle
            else:
                low=middle+1
            
