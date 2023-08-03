#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1] = 1
        memo[2] = 2

        def climb(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = climb(n-1) + climb(n-2)
                return memo[n]
        return climb(n)
# @lc code=end
1,2,3,5,8,