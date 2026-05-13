# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        result = []

        if not root:
            return 0

        while q:
            level = []
            level_size = len(q)

            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)

                if not node.left and not node.right:
                    return len(result)+1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(level)

        print(result)