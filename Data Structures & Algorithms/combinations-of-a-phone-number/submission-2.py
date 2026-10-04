class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_map={'2':('a','b','c'),
        '3':('d','e','f'),
        '4':('g','h','i'),
        '5':('j','k','l'),
        '6':('m','n','o'),
        '7':('p','q','r','s'),
        '8':('t','u','v'),
        '9':('w','x','y','z'),
        }
        res=[]

        def backtrack(idx,currStr):
            if idx==len(digits):
                res.append(currStr)
                return
            for c in num_map[digits[idx]]:
                backtrack(idx+1, currStr+c)
        if digits:
            backtrack(0,"")

        return res
            
        