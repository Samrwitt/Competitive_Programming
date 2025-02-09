class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        result = math.isqrt(num) 
        return result * result == num
