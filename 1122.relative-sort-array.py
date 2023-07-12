#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#
from typing import List
# @lc code=start


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_counter = collections.Counter(arr1)
        res = []
        for i in arr2:
            res += [i]*arr1_counter.pop(i)
        return res + sorted(arr1_counter)


solution = Solution().relativeSortArray(
    arr1=[],
    arr2=[]
)
print("Solution :", solution)
# @lc code=end
