class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        j = m

        for i in range(n - m + 1):
            curr_str = haystack[i:j]
            if (curr_str == needle):
                return i
            j += 1

        return -1