from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        all_nums = set()
        for n in nums:
            if n in all_nums:
                return True
            else:
                all_nums.add(n)
        return False
