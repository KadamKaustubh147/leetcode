class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []
        used = [False] * len(nums)

        def backtrack():

            # If permutation complete
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):

                # Skip if already used
                if used[i]:
                    continue

                # Choose
                used[i] = True
                curr.append(nums[i])

                # Explore
                backtrack()

                # Un-choose (backtrack)
                curr.pop()
                used[i] = False


        backtrack()
        return res