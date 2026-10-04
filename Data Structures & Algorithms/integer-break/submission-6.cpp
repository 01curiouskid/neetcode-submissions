class Solution {
public:
    vector<int>dp;
    int dfs(int num){
            if (dp[num]!=-1){
                return dp[num];
            }
            int res=0;
            int val;
            for (int i=1;i<num;i++){
                val=max(i*(num-i),i*dfs(num-i));
                res=max(val,res);
            }
            return dp[num]=res;
        }
    int integerBreak(int n) {
        dp=vector<int>(n+1,-1);
        dp[1]=dp[2]=1;
        return dfs(n);
    }
};