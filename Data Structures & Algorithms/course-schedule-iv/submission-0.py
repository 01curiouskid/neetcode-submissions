class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preMap=defaultdict(list)
        indegree=[0]*numCourses
        for a,b in prerequisites:
            preMap[a].append(b)
            indegree[b]+=1
        isPrereq=[[False]*numCourses for _ in range(numCourses)]   
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while q:
            crs=q.popleft()
            for nxt in preMap[crs]:
                isPrereq[crs][nxt]=True
                for u in range(numCourses):
                    if isPrereq[u][crs]:
                        isPrereq[u][nxt]=True
                indegree[nxt]-=1
                if indegree[nxt]==0:
                    q.append(nxt)
        res=[]
        for u,v in queries:
            res.append(isPrereq[u][v])
        return res