from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence={char: idx for idx, char in enumerate(s)}
        start=end=0
        partition=[]

        for idx, char in enumerate(s):
            end = max(end, last_occurence[char])
            if idx==end:
                partition.append(end-start+1)
                start= idx+1
        return partition