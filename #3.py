## Longest Substring Without Repeating Characters - Medium

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        total = 0
        left = 0
        chars = set()
        
        for right in range(len(s)):
            if s[right] not in chars:
                chars.add(s[right])
                total = max(total, right - left + 1)
            else:
                while s[right] in chars:
                    chars.remove(s[left])
                    left += 1
                chars.add(s[right])

        return total
    
## Took time because I forgot about sets