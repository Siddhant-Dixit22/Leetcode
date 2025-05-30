class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort()
        longest = ""

        for word in dictionary:
            s_poi = 0
            word_poi = 0

            while (s_poi < len(s) and word_poi < len(word)):
                if (s[s_poi] == word[word_poi]):
                    word_poi += 1
                s_poi += 1
            
            if (word_poi >= len(word)):
                if (len(word) > len(longest)):
                    longest = word
        
        return longest