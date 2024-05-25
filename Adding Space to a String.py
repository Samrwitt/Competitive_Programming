from typing import List;
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        space_index = 0
        n = len(spaces)
        
        for i in range(len(s)):
            # Check if the current index matches the space index
            if space_index < n and i == spaces[space_index]:
                result.append(' ')
                space_index += 1
            result.append(s[i])
        
        return ''.join(result)
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        space_index = 0
        n = len(spaces)
        
        for i in range(len(s)):
            if space_index < n and i == spaces[space_index]:
                result.append(' ')
                space_index += 1
            result.append(s[i])
        
        return ''.join(result)
