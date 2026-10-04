class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        window=len(s1)
        count_s1=Counter(s1)
        count_s2=Counter(s2[:window])
        if count_s2==count_s1:
                return True
        for i in range(1,len(s2)-window+1):
            count_s2[s2[i+window-1]] = 1+count_s2.get(s2[i+window-1],0)
            count_s2[s2[i-1]]-=1
            if count_s2==count_s1:
                return True
        return False
            
            