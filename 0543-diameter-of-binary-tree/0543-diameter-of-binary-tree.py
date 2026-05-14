# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root):

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            # we use res as the path may or may not pass thru the root node
            self.res = max(self.res,left+right)

            # we return the height --> and res contains the maximum diameter --> path length bw two nodes
            return 1 + max(left,right)
        
        dfs(root)
        return self.res
