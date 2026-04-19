# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res= []
        def dfs(n,lvl):
            if not n:
                return None
            if len(res)==lvl:
                res.append([])
            res[lvl].append(n.val)
            dfs(n.left,lvl +1)
            dfs(n.right,lvl +1)
        dfs(root,0)
        return res
