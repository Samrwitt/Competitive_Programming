class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverse = 0
        original = x
        
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x //= 10

        return x == reverse or x == reverse // 10
