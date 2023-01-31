from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonzero = [val for val in nums if val != 0]
        max_ind = len(nonzero) - 1
        for i in range(len(nums)):
            nums[i] = nonzero[i] if i <= max_ind else 0
