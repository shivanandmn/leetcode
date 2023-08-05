#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for row in range(1, numRows):
            current_row = [1]
            # print(row)
            for col in range(1, row):
                prev_row = triangle[row - 1]
                current_row.append(prev_row[col - 1] + prev_row[col])
            current_row.append(1)
            # print(current_row)
            triangle.append(current_row)
        return triangle
        
# @lc code=end

