# Bucket sort solution

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash
        mp = defaultdict(int)

        for num in nums:
            mp[num] += 1
        
        # print(mp)
        # building reverse mapping --> frequency to the list of numbers
        new_mp = [[] for _ in range(len(nums)+1)]
        print(mp)
        for num,count in mp.items():
            new_mp[count].append(num)

        print(new_mp)
        
        # now we want top k frequent elements
        # count = 0
        ans = []
        for i in range(len(new_mp)-1, 0, -1):
            for num in new_mp[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans



        

