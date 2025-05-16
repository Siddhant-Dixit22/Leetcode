class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L <= R:
            if(s[L].isalnum() and s[R].isalnum()):
                if (s[L].lower() != s[R].lower()):
                    return False
                L += 1
                R -= 1
            else:
                if (s[L].isalnum()):
                    R -= 1
                else:
                    L += 1
        
        return True