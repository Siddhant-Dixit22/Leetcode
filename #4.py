class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_arr = []

        for i in range(len(nums1)):
            merged_arr.append(nums1[i])

            
        for i in range(len(nums2)):
            merged_arr.append(nums2[i])

        merged_arr.sort()

        if (len(merged_arr) % 2 != 0):
            return(merged_arr[math.floor((len(merged_arr))/2)])
        else:
            return((merged_arr[(math.floor((len(merged_arr)-1)/2))] + merged_arr[math.floor((len(merged_arr))/2)])/2)
        
## Not optimal, need to get O(log(m+n)), binary search needed, need to do in future.