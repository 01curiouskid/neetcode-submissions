class Solution:
    def numSquares(self, n: int) -> int:
        dp={}
        def dfs(target):
            if target==0:
                return 0
            if target in dp:
                return dp[target]
            
            res=target
            for i in range(1, target):
                if i*i>target:
                    break
                res = min( res, 1+dfs(target- i*i))
            dp[target]=res
            return res
        return dfs(n)