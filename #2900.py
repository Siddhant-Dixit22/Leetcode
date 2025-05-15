class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ret = []
        ret.append(words[0])
        n = len(words)

        for i in range(1, n):
            if (groups[i] != groups[i-1]):
                ret.append(words[i])
        

        return ret