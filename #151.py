class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        L, R = 0, len(words) - 1

        while L < R:
            words[L], words[R] = words[R], words[L]
            L += 1
            R -= 1

        return " ".join(words) 