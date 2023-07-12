#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] > target:
                end = mid-1
            elif nums[mid] == target:
                return mid
            else:
                start = mid+1
        return start


solution = Solution().searchInsert(
    nums=[1, 3, 5, 6],
    target=2
)
print("Solution :", solution)
# @lc code=end
