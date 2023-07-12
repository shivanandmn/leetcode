#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        while start <= end:
            mid = start + (end - start)//2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid + 1
            else:
                end = mid - 1
        return end


# @lc code=end
if __name__ == "__main__":
    solution = Solution().mySqrt(
        x=10
    )
    print("Solution :", solution)
    print()
