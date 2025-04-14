## Reverse Integer - Medium

class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if (x < 0):
            is_negative = True
        
        curr_num = abs(x)
        str_num = str(curr_num)
        reversed_num = ""

        for i in reversed(str_num):
            reversed_num += i

        reversed_num = int(reversed_num)

        if ((reversed_num > (2**31 - 1)) or (reversed_num < (-2**31))):
            return 0

        if is_negative:
            reversed_num = -reversed_num

        return reversed_num