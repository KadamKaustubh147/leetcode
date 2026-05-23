class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        # x can be outside the range --> y needs to be in the range
        # finding the rightmost number
        low,high = 0,r
        ans = -1
        while low <= high:
            mid = (low+high)//2

            if mid**k <= r:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        ans_r = ans
        ans = -1

        low,high = 0,r        

        while low<=high:
            mid = (low+high)//2

            if mid**k >= l:
                ans = mid
                high = mid -1
            else:
                low = mid+1
        
        ans_l = ans


        return ans_r - ans_l + 1
            
            
            