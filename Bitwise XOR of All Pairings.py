from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1, xor2 = 0, 0
        
        # XOR all elements in nums1 and nums2
        for num in nums1:
            xor1 ^= num
        for num in nums2:
            xor2 ^= num
        
        # Determine the overall XOR
        if len(nums2) % 2 == 0 and len(nums1) % 2 == 0:
            return 0  # All contributions cancel out
        elif len(nums2) % 2 == 0:
            return xor2  # nums1 contributions cancel out
        elif len(nums1) % 2 == 0:
            return xor1  # nums2 contributions cancel out
        else:
            return xor1 ^ xor2  # Both contribute

