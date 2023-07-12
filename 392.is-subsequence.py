#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            elif s[i] != t[j]:
                j += 1
        if i == len(s):
            return True
        else:
            return False


solution = Solution().isSubsequence(
    s="axc",
    t="ahbgdc"
)
print("Solution :", solution)
# @lc code=end
