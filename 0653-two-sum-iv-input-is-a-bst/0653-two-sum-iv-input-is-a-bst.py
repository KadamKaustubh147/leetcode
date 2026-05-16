# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # traversing the BST

        if not root:
            return False

        nodes = set()

        def dfs(root):
            if not root:
                return
            nodes.add(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        for num in nodes:
            if k-num in nodes and k-num!=num:
                return True
        
        return False