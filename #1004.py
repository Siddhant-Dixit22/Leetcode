class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        L, R = 0, 0

        while R < len(nums):
            if (nums[R] == 0):
                k -= 1
            if (k < 0):
                while (nums[L] != 0):
                    L += 1
                L += 1
                k += 1
            max_len = max(max_len, R - L + 1)
            R += 1
        

        return max_len