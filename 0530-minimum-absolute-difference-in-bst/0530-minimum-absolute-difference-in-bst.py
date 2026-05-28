# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # O(n^2) solution --> for a normal tree and brute force solution
        # Can we have less difference ---> can greedy approach work?

        # in bst inorder traversal gives nodes in sorted order

        # O(n) + O(n)

        nums = []

        curr = root

        def inorder(curr):
            if not curr:
                return
            inorder(curr.left)
            nums.append(curr.val)
            inorder(curr.right)
        
        inorder(curr)

        # now nums is a sorted array

        mini = 1e6
        i=0

        # print(nums)

        while i+1<len(nums):
            mini = min(mini, nums[i+1]-nums[i])
            # print(mini)
            i+=1
        
        return mini






