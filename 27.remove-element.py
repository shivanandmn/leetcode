#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[slow] = nums[i]
                slow+=1
        return slow

        
# @lc code=end

