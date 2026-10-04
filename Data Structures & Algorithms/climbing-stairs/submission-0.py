class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[1,2]
        if n<=2:
            return n
        i=2
        for _ in range(i,n):
            temp=dp[1]
            dp[1]=dp[1]+dp[0]
            dp[0]=temp
        return dp[1]