# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         return len([c for c in "{0:b}".format(n) if c == "1"])


# trivialized by python
class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()

# cool bitwise version

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         ans = 0
#         while n:
#             n &= n - 1
#             ans += 1
#         return ans
