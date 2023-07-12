#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
from typing import List

# @lc code=start


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        result = []
        i, j = 0, 0
        while (i < nums1_len) and (j < nums2_len):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        return result


solution = Solution().intersect(
    nums1=[1, 2, 2, 1],
    nums2=[2, 2]
)
print("Solution :", solution)
print()
# @lc code=end
