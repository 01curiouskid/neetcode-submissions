class Solution {
public:
    vector<vector<int>>dp;
    int dfs(vector<vector<int>>& grid, int i, int j){
        int m=grid.size();
        int n=grid[0].size();
        if (i>=m || j>=n) return INT_MAX;
        if (i==m-1 && j==n-1) return grid[i][j];
        if (dp[i][j]!= -1) return dp[i][j];
        return dp[i][j] = grid[i][j]+min(dfs(grid, i+1, j),dfs(grid,i,j+1));
    }
    int minPathSum(vector<vector<int>>& grid) {
        int m=grid.size();
        int n=grid[0].size();
        dp=vector<vector<int>>(m+1,vector<int>(n+1,-1));
        return dfs(grid,0,0);   
    }
};