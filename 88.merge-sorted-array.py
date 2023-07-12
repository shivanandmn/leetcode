#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:len(nums2)]
        counter = 0
        for n in nums2:
            for i in range(len(nums1)-1):
                if n<nums1[i+1] and n>=nums1[i]:
                    nums1.insert(i, n)
                    break
                counter+=1
            print(n)
            if counter==m:
                nums1.append(n)

                    
            
# @lc code=end

