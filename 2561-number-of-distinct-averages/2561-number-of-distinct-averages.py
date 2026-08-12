class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1

        averages = set()

        while left < right:
            average = (nums[right] + nums[left]) / 2
            averages.add(average)

            left +=1
            right -=1

        return len(averages)
        