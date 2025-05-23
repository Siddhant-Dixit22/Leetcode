class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x):
            curr_sum = 0

            while x:
                digit = x % 10
                curr_sum += digit ** 2
                x = x // 10
            
            return curr_sum

        visited = set()
        
        while n not in visited:
            visited.add(n)
            n = next_num(n)
            if n == 1:
                return True

        return False