class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # child --> parent mapping
        parent = {
            root: None
        }

        queue = deque()
        queue.append(root)

        # jab tak p or q nai pahoch jaate tabh tak har node ke parent store karo
        while not (p in parent and q in parent):
            node = queue.popleft()

            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)
            
        ancestors = set()

        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q not in ancestors:
            q = parent[q]
        
        return q
