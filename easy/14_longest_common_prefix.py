from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        m = min([len(s) for s in strs])
        for i, c in enumerate(strs[0]):
            if i == m or any(s[i] != c for s in strs):
                break
            else:
                ret = f"{ret}{c}"
        return ret
