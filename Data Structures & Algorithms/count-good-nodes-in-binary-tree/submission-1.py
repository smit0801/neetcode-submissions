# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def inorder(node,mtn):
            if not node:
                return 0
            res= 1 if node.val >= mtn else 0
            mtn=max(mtn,node.val)
            res += inorder(node.left,mtn)
            res += inorder(node.right,mtn)
            return  res
        return inorder(root,root.val)
