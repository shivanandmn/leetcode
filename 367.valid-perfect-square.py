#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0:
            return 0
        else:
            start = 0
            end = num
            while start <= end:
                mid = start + (end-start)//2
                if (mid * mid) == num:
                    return True
                elif (mid * mid) < num:
                    start = mid + 1
                else:
                    end = mid - 1
            return False


solution = Solution().isPerfectSquare(
    num=16
)
print("Solution :", solution)
print()
# @lc code=end
