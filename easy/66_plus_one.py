from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = 0
        for i, n in enumerate(digits[::-1]):
            s += 10 ** i * n
        s += 1
        return [int(x) for x in str(s)]
