class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1
        arr = nums
        n = len(arr)
        if(arr[0]<arr[n-1]):
            return arr[0]

        while lo <= hi:
            mid = (lo + hi)//2

            # mid should be chota on left and right both sides then only it is minimum element

            # % is done such that if prev and next (mid+1) and (mid-1) don't become out of bounds --> rotated array is cylic kinda in nature
            if (arr[(mid+n-1) % n] >= arr[mid]) and (arr[mid] <= arr[(mid+1)%n]):
                return arr[mid]
            
            # now for other elements one half is sorted and the other half is unsorted

            # if sorted half --> go in the unsorted half
            # don't compare mid with low or high compare it with start and end --> more logical and gives correct answer
            elif arr[0] <= arr[mid]:
                lo = mid+1
            elif arr[n-1] >= arr[mid]:
                hi = mid-1
            else:
                return -1
