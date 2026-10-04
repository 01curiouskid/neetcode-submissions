class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        for num in nums:
            count[num]+=1

        arr=[]
        for n,c in count.items():
            arr.append((c,n))
        arr.sort()
        res=[]
        for i in range(-k,0):
            res.append(arr[i][1])
        return res