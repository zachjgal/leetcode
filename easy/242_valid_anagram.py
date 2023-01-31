
def char_occurrences(s: str) -> dict:
    """e.g. 'anagram' -> {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1} """
    freqs = {}
    for c in s:
        if c in freqs:
            freqs[c] += 1
        else:
            freqs[c] = 1
    return freqs


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        return char_occurrences(s) == char_occurrences(t)
