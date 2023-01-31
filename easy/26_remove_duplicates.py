from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print(nums)
        seen = set()
        new = []
        for n in nums:
            if n not in seen:
                new.append(n)
                seen.add(n)

        i = 0
        for n in new:
            nums[i] = n
            i += 1
        return i
