# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encrypt=''
        def dfs(node):
            nonlocal encrypt
            if not node:
                encrypt=encrypt +  ","+ str("NULL")
                return
            encrypt=encrypt +  ","+ str(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return encrypt[1:]


      


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.index=0
        def dfs():
            if vals[self.index] == "NULL":
                self.index +=1
                return None
            node= TreeNode(int(vals[self.index]))
            self.index +=1
            node.left = dfs()
            node.right= dfs()
            return node
        return dfs()
