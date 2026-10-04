class Solution {
public:
    vector<vector<int>>dp;
    int dfs(int i,int total, vector<int>& stones){
        int sumStones= accumulate(stones.begin(),stones.end(),0);
        int target=ceil(sumStones/2);
        if (total>=target || i==stones.size()){
            return abs(total -(sumStones-total));
        }
        if(dp[i][total]!=-1){
            return dp[i][total];
        }
        dp[i][total] =min(
            dfs(i+1, total, stones), dfs(i+1, total+stones[i], stones)
        );
        return dp[i][total];
        }
    int lastStoneWeightII(vector<int>& stones) {
        int sumStones= accumulate(stones.begin(),stones.end(),0);
        int target=ceil(sumStones/2);
        dp= vector<vector<int>>(stones.size(), vector<int>(target+1,-1));
        return dfs(0,0,stones);

        
        
    }
};