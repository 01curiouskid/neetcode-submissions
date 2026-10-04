class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=''
        i=0
        while i<len(strs[0]):
            char=strs[0][i]
            for w in strs:
                if i>=len(w) or char!=w[i]:
                    return res
            res=res+char
            i+=1
        return res
            