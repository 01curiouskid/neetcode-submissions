class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        visited=set()
        def backtrack(row,col,idx):
            if idx==len(word):
                return True
            if (row<0 or col<0 or row>=rows or col>=cols or word[idx]!=board[row][col] or (row,col) in visited):
                return False
            visited.add((row,col))
            res=(backtrack(row+1,col,idx+1) or backtrack(row-1,col,idx+1) or backtrack(row,col-1,idx+1) or backtrack(row,col+1,idx+1))
            visited.remove((row,col))
            return res

        for row in range(rows):
            for col in range(cols):
                if backtrack(row,col,0):
                    return True
        return False
