class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = []
        i, j = 0, 0
        n, m = len(word1), len(word2)
        
        while i < n or j < m:
            if i < n and (j >= m or word1[i:] > word2[j:]):
                merge.append(word1[i])
                i += 1
            else:
                merge.append(word2[j])
                j += 1
        
        return ''.join(merge)