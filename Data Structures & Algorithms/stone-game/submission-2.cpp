class Solution {
public:
    vector<vector<int>> dp;
    int dfs(vector<int>& piles, int start, int end){
        if (start==end){
            return piles[start];
        }
        if (dp[start][end]!=-1){
            return dp[start][end];
        }
        return dp[start][end]=max(piles[start]-dfs(piles, start+1, end), piles[end]-dfs(piles, start, end-1));
    }
    bool stoneGame(vector<int>& piles) {
        int n=piles.size();
        dp.resize(n, vector<int>(n,-1));
        int res= dfs(piles, 0, n-1);
        if(res>0) return true;
        else return false;
    }
};