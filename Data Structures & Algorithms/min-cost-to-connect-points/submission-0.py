class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        adj=defaultdict(list)
        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        #Prim's
        # print(adj)
        minheap=[[0,0]]
        visited=set()
        cost=0
        while len(visited)<n:
            dist, node= heapq.heappop(minheap)
            if node in visited:
                continue
            cost+=dist
            visited.add(node)
            for nei in adj[node]:
                if nei[1] not in visited:
                    heapq.heappush(minheap,nei)
        return cost


                
