class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        count = 0
        j = 0

        for i in range(n):
            if (nums[i] != val):
                nums[j] = nums[i]
                j += 1
                count += 1
        
        return count