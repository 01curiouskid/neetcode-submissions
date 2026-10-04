class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge=trust[0][1]
        for i in range(1,len(trust)):
            if trust[i][1]!=judge:
                return -1
        return judge