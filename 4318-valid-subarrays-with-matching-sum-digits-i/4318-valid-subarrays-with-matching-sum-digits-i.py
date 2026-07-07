class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n = len(nums)
        prefix = [0]*(n+1)

        for i,num in enumerate(nums):
            prefix[i+1] = prefix[i] + num
        
        # finding valid subarrays

        count = 0
        for i in range(n):
            for j in range(i,n):
                sub_array_sum = prefix[j+1]-prefix[i]

                if int(str(sub_array_sum)[0]) == x and int(str(sub_array_sum)[-1]) == x:
                    count += 1
        
        return count
