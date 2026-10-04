class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        q=deque()
        q.append(0)
        visited=set()
        visited.add(0)
        step=0
        while q:
            for _ in range(len(q)):
                idx=q.popleft()
                
                for i in range(1,nums[idx]+1):
                    if (idx+i)>=len(nums)-1:
                        return step+1
                    if (idx+i) not in visited:
                        q.append(idx+i)
                        visited.add(idx+i)
            step+=1