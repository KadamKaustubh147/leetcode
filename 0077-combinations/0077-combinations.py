class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr = []

        def backtrack(i):
            if len(curr) == k:
                res.append(curr.copy())
                return
            
            while i <= n:
                curr.append(i)
                backtrack(i+1)
                curr.pop()

                i+=1
        
        backtrack(1)
        return res