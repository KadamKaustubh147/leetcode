# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # level order traversal
        q = deque()
        result = []
        q.append(root)

        while q:
            level = 0
            level_size = len(q)

            for _ in range(level_size):
                node = q.popleft()
                level += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(level/level_size)
        
        return result
