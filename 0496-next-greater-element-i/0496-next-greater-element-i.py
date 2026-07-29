class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = [-1]*len(nums2)

        st = []

        for i in range(len(nums2)):
            while st and nums2[st[-1]] < nums2[i]:
                next_greater[st[-1]] = i
                st.pop()
            
            st.append(i)

        n = len(nums1)
        res = [-1]*n

        print(next_greater)

        for i in range(len(next_greater)):
            next_greater[i] = nums2[next_greater[i]] if next_greater[i] != -1 else -1

        mp = defaultdict(int)
        # number to index

        for i,num in enumerate(nums2):
            mp[num] = next_greater[i]
        
        res = []

        for num in nums1:
            res.append(mp[num])

        return res


