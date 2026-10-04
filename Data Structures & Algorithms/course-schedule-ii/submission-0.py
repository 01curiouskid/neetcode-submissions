from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Build adjacency list (course → list of prerequisites)
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()    # current DFS path (to detect cycles)
        visited = set()     # nodes we've already added to result
        res = []            # stores post-order result

        def dfs(crs):
            if crs in visiting:
                return False  # cycle detected
            if crs in visited:
                return True   # already processed

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)

            visited.add(crs)
            res.append(crs)  # post-order: add after all prereqs
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []  # cycle detected

        return res  # reverse post-order to get valid order
