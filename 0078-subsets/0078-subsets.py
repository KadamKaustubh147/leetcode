from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []
        n = len(nums)

        def backtrack(start):

            # print(f"\nENTER backtrack(start={start})")
            # print("  curr =", curr)

            # Save current subset
            res.append(curr.copy())
            # print("  ADD to res ->", curr.copy())
            # print("  res =", res)

            i = start
            while i < n:

                # Choose
                curr.append(nums[i])
                # print(f"\n  PUSH {nums[i]} -> curr =", curr)

                # Explore
                backtrack(i + 1)

                # Un-choose (backtrack)
                popped = curr.pop()
                # print(f"  POP {popped} -> curr =", curr)

                i += 1

            # print(f"EXIT backtrack(start={start}) with curr =", curr)

        backtrack(0)
        return res
