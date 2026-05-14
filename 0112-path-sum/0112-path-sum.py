# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(node,sum):
            # since there is no node to contribute to the sum we return False ig this is edge case
            if not node:
                return False
            sum += node.val
            # if leaf
            if not node.right and not node.left:
                return sum==targetSum
            # carrying out the dfs further since there is a return value for this function and we need only one path
            # therefore we use OR

            return dfs(node.right,sum) or dfs(node.left,sum)
        
        return dfs(root,0)

        