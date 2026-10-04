class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start='0000'
        if start in deadends:
            return -1
        def children(lock):
            res=[]
            for i in range(4):
                dig=str((int(lock[i])+1)%10)
                res.append(lock[:i]+dig+lock[i+1:])
                dig=str((int(lock[i])-1)%10)
                res.append(lock[:i]+dig+lock[i+1:])
            return res
        q=deque()
        q.append((start,0))
        visit=set(deadends)
        while q:
            node, turns=q.popleft()
            if node==target:
                return turns
            for child in children(node):
                if child not in visit:
                    q.append((child,turns+1))
                    visit.add(child)
        return -1

