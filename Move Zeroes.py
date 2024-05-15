from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast=0
        slow=0
        while fast<len(nums):
            if nums[fast]!=0:
                nums[slow], nums[fast]=nums[fast], nums[slow]
                slow+=1
            fast+=1