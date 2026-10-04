class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        pacific=[[False]*cols for _ in range(rows)]
        atlantic=[[False]*cols for _ in range(rows)]
        if not heights:
            return []
        def dfs(row,col,visited,prev_height):
            if (row<0 or col<0 or row==rows or col==cols or visited[row][col] or heights[row][col]<prev_height):
                return
            visited[row][col]=True
            for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                dfs(row+dr, col+dc, visited, heights[row][col])
            
        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, cols-1, atlantic, heights[row][cols-1])
        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])
            dfs(rows-1, col, atlantic, heights[rows-1][col])
        result=[]
        for row in range(rows):
            for col in range(cols):
                if pacific[row][col] and atlantic[row][col]:
                    result.append([row,col])
        return result
