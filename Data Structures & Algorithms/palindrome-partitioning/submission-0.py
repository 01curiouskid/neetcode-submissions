class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res,part=[],[]
        def backtrack(i):
            if i>=len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if self.ispalindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()
        backtrack(0)
        return res
    def ispalindrome(self,string):
        if string==string[::-1]:
            return True
        return False