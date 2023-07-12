#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
def add(x):
    if x==9:
        return [1, 0]
    else:
        return [x+1]

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        prev = 0
        if digits[-1]!=9:
            digits[-1] = digits[-1] + 1
            return digits
        else:
            for i in range(-1, -len(digits)-1, -1):
                # print(i)
                if digits[i]==9:
                    digits[i] = 0
                    prev = 1
                else:
                    digits[i] +=1
                    prev = 0
                    break
        # print(prev)        
        if prev:
            digits = [1] + digits
        return digits
            
# @lc code=end

