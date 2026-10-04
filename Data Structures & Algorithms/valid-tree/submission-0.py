class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)>n-1:
            return False
        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=set()
        def dfs(vertex,prev):
            if vertex in visited:
                return False
            visited.add(vertex)
            for nei in adj[vertex]:
                if nei==prev:
                    continue
                if not dfs(nei,vertex):
                    return False
            return True
        return dfs(0,-1) and len(visited)==n    
             
