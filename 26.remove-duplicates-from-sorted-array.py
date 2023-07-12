#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for i in range(len(nums)):
            if nums[slow] != nums[i]:
                slow +=1
                nums[slow]=nums[i]
        return slow+1




        
# @lc code=end

