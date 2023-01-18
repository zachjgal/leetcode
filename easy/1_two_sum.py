from typing import List, Tuple


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Tuple[int, int]:
        m = {}
        for i, n in enumerate(nums):
            if target - n in m:
                return m[target - n], i
            m[n] = i
