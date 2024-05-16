from typing import List
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(sub_arr, k):
            return sub_arr[:k][::-1] + sub_arr[k:]

        n = len(arr)
        result = []

        for size in range(n, 1, -1):

            max_idx = arr.index(size)

            if max_idx != size - 1:
                if max_idx != 0:
                    result.append(max_idx + 1)
                    arr = flip(arr, max_idx + 1)
                result.append(size)
                arr = flip(arr, size)

        return result
