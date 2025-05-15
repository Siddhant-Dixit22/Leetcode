class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = 1, 0
        
        while i < n:
            if (nums[i] < nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
                i = 1
                j = 0
            else:
                i += 1
                j += 1


### Solution is suboptimal, better solution uses 3 pointers, or the 3-way partitioning algorithm