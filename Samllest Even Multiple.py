class Solution:
    def gcf(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def smallestEvenMultiple(self, n: int) -> int:
        sem = (2 * n) // self.gcf(2, n)
        return sem
