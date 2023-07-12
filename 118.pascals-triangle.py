#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        for i in range(1, numRows):
            left, right = out[i][0], right[i][-1]
            out.append()
        return out
            
# @lc code=end

