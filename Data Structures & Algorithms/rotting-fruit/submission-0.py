class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols= len(grid),len(grid[0])
        fresh=set()
        rotten=deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==2:
                    rotten.append((row,col))
                if grid[row][col]==1:
                    fresh.add((row,col))
        def addFruit(row,col):
            if (row<0 or col<0 or row==rows or col==cols or grid[row][col]==0 or grid[row][col]==2 ):
                return 0
            grid[row][col]=2
            rotten.append((row,col))
            fresh.remove((row,col))
            return 1
        minute=0
        
        while rotten and fresh:
            for i in range(len(rotten)):
                print(fresh)
                print(rotten)
                row,col=rotten.popleft()
                addFruit(row+1,col)
                addFruit(row-1,col)
                addFruit(row,col+1)
                addFruit(row,col-1)
            minute+=1
        if fresh:
            return -1
        return minute

