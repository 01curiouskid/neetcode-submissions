class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp=[[0]*(amount+1) for _ in range(len(coins)+1)]

        # for i in range(len(coins)+1):
        #     dp[i][0]=1
        
        # for c in range(len(coins)-1,-1,-1):
        #     for amt in range(1,amount+1):
        #         dp[c][amt] = dp[c+1][amt]
        #         if amt-coins[c]>=0:
        #             dp[c][amt] += dp[c][amt-coins[c]]
                    
        # return dp[0][amount]

        dp=[0]*(amount+1)
        dp[0]=1
        for i in range(len(coins)-1,-1,-1):
            for amt in range(1, amount+1):
                dp[amt] +=dp[amt-coins[i]] if coins[i]<=amt else 0
        return dp[amount]
            


