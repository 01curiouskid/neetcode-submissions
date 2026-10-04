# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ##Recursive DFS
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

        ##Iterative DFS
        # stack=[[root,1]]
        # res=0
        # while stack:
        #     node,depth=stack.pop()
        #     if node:
        #         res=max(res,depth)
        #         stack.append([node.left,1+depth])
        #         stack.append([node.right,1+depth])
        # return res

        ##BFS
        q=deque()
        res=0
        if root:
            q.append(root)
        while q:
            for _ in range(len(q)): #This loop processes all nodes at the current level of the tree.
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res+=1
        return res
        