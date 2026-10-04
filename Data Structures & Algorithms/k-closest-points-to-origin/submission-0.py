class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        for pt in points:
            dist=pt[0]**2 + pt[1]**2
            heapq.heappush(minheap, (dist,pt))
        res=[]
        for _ in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res