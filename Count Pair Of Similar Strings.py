from typing import List
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        def are_similar(word1: str, word2: str) -> bool:
            return set(word1) == set(word2)
        
        similar_count = 0
        n = len(words)
        
        for i in range(n):
            for j in range(i+1, n):
                if are_similar(words[i], words[j]):
                    similar_count += 1
        
        return similar_count
        
        return similar_count
