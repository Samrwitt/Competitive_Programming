class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        values = set(nums)
        count = 0

        for num in nums:
            if num - diff in values and num + diff in values:
                count +=1

        return count
        