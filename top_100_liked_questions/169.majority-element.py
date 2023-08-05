#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        record = {}
        l = len(nums)
        for n in nums:
            if n not in record:
                record[n] = 1
            else:
                record[n]+=1
                if record[n]>(l/2):
                    return n
        return n
                
        
# @lc code=end

