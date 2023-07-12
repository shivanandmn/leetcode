#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx,num in enumerate(nums):
            seen[num] = idx
            if target-num in seen:
                return [idx, seen[target-num]]
            else:
                seen[num] = idx


        
# @lc code=end
