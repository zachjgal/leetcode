
def sqsum(n):
    s = 0
    k = n
    while k != 0:
        s += (k % 10) ** 2
        k = k // 10
    return s


class Solution:
    def isHappy(self, n: int) -> bool:
        past = set()
        while n != 1:
            if n in past:
                return False
            newn = sqsum(n)
            past.add(n)
            n = newn

        return True
