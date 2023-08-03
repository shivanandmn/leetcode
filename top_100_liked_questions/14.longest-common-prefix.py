#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    # 87% runtime, 35.14% memory usage, of all submissions
    def longestCommonPrefix(self, strs: List[str]) -> str:
        init = sorted(strs, key=lambda x: len(x))[0]
        res = ""
        for idx,s in enumerate(init):
            c = 0
            for j in strs:
                if s==j[idx]:
                    c+=1
            if c==len(strs):
                res +=s
            else:
                break
        return res
    
    # ## 97% runtime, 71.14% memory usage, of all submissions
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     l = list(zip(*strs))
    #     prefix = ""
    #     for i in l:
    #         if len(set(i))==1:
    #             prefix += i[0]
    #         else:
    #             break
    #     return prefix
# @lc code=end

