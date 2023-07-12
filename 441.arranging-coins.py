#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
def gauss(x):
    return x*(x+1)/2


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # return int((-1 + (1 + 8*n) ** 0.5) // 2)
        start = 0
        end = n
        res = 0
        while start <= end:
            mid = start + (end-start)//2
            if gauss(mid) > n:
                end = mid - 1
            else:
                start = mid + 1
                res = max(mid, res)
        return res


solution = Solution().arrangeCoins(
    n=8
)
print("Solution :", solution)
# @lc code=end
