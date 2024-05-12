from typing import List
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        total_skill = sum(skill)
        
        if total_skill % (n // 2) != 0:
            return -1
        
        target_skill = total_skill // (n // 2)
        
        skill.sort()
        
        chemistry = 0
        left, right = 0, n - 1
        
        while left < right:
            team_skill = skill[left] + skill[right]
            if team_skill != target_skill:
                return -1
            chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return chemistry
          
        