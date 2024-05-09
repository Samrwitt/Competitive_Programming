from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = [0] * 101  # Since nums[i] <= 100
        for num in nums:
            counts[num] += 1

        prefix_sum = [0] * 101
        for i in range(1, 101):
            prefix_sum[i] = prefix_sum[i - 1] + counts[i - 1]

        result = []
        for num in nums:
            result.append(prefix_sum[num])

        return result