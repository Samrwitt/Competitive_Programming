class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        existing = set(nums)
        missing = []

        for num in range(1, len(nums) +1):
            if num not in existing:
                missing.append(num)
                
        return missing



        