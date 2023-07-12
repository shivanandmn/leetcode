#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 0
        end = n
        while start < end:
            mid = start + (end-start)//2
            if guess(mid) == -1:
                end = mid - 1
            elif guess(mid) == 1:
                start = mid + 1
            else:
                return mid
        return start


solution = Solution().guessNumber(
    n=10
)
# @lc code=end
