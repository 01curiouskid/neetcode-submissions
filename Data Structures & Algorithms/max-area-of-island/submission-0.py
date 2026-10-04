class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols= len(grid), len(grid[0])
        visit=set()
        
        def bfs(r,c):
            
            q=deque()
            visit.add((r,c))
            q.append((r,c))
            area=0

            while (q):
                r,c =q.popleft()
                area+=1
                direc=[[0,1],[1,0],[0,-1],[-1,0]]
                for dr, dc in direc:
                    nr=r+dr
                    nc=c+dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc]==1 and (nr,nc) not in visit):
                        q.append((nr,nc))
                        visit.add((nr,nc))
                        
            return area
        max_area=0
        for r in range(rows):
            for c in range(cols): 
                if grid[r][c]==1 and (r,c) not in visit:
                    area=bfs(r,c)
                    max_area=max(area,max_area)
        return max_area
        
        