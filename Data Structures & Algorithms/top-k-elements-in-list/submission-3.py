class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #O(nlogn)
        # count=defaultdict(int)
        # for num in nums:
        #     count[num]+=1

        # arr=[]
        # for n,c in count.items():
        #     arr.append((c,n))
        # arr.sort()
        # res=[]
        # for i in range(-k,0):
        #     res.append(arr[i][1])
        # return res

        count=defaultdict(int)
        for num in nums:
            count[num]+=1
        heap=[]
        for n,c in count.items():
            heapq.heappush(heap, (c,n))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res