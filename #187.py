class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        ret = []
        L = 0
        prev_seqs = set()

        for R in range(10, len(s) + 1):
            if (s[L:R] in prev_seqs and s[L:R] not in ret):
                ret.append(s[L:R])
            prev_seqs.add(s[L:R])
            L += 1
        
        return ret