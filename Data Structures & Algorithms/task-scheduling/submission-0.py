class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxHeap=[-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        queue=deque() #pairs of [-cnt,time]
        time=0

        while maxHeap or queue:
            time+=1
            if maxHeap:
                  cnt = 1 + heapq.heappop(maxHeap)
                  if cnt<0: #task left
                    queue.append([cnt,time+n])
            if queue and queue[0][1]==time:
                heapq.heappush(maxHeap,queue.popleft()[0])
        return time


         