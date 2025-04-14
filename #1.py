## Two Sum - Easy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = [] * 2

        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i + 1, len(nums)):
                if (target == (nums[j] + curr)):
                    sol.append(i)
                    sol.append(j)
                    return sol
                


## Brute Force Way, Need to learn and study DSA