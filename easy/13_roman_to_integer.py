class Solution:
    def romanToInt(self, s: str) -> int:
        mapping_1 = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        mapping_2 = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            }
        ptr = 0
        total = 0
        l = len(s)
        while ptr < l:
            # try to match to the length 2 nums
            if ptr < l - 1:
                subset = s[ptr:ptr+2]
                if subset in mapping_2:
                    total += mapping_2[subset]
                    ptr += 2
                    continue
            subset = s[ptr]
            total += mapping_1[subset]
            ptr += 1
        return total
