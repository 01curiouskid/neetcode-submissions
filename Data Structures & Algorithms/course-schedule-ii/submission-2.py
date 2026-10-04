class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap=defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # a course can have 3 possible outcomes
        # visited
        #visiting
        #unvisited
        result=[]
        visited=set()
        path=set()
        def dfs(crs):
            if crs in path:
                return False
            if crs in visited:
                return True
            path.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            path.remove(crs)
            visited.add(crs)
            result.append(crs)
            return True
        for crs in range (numCourses):
            if not dfs(crs):
                return []
        return result

        