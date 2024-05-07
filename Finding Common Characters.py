from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_chars = []
        char_freq = {}
        for char in words[0]:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        for char in char_freq:
            min_count = char_freq[char]
            
            for word in words[1:]:
                count = word.count(char)
                min_count = min(min_count, count)
            
            common_chars.extend([char] * min_count)
        
        return common_chars