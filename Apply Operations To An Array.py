from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                i += 2 
            else:
                i += 1 
        result = [num for num in nums if num != 0]
        result += [0] * (len(nums) - len(result))
        
        return result
    