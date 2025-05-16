class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        curr_set = set()
        for n in nums:
            if n in curr_set:
                return True
            curr_set.add(n)

        return False