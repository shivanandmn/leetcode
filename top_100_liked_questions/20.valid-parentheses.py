#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        start = {
            "(":")",
            "{":"}",
            "[":"]",
        }
        tracker = Tracker()
        for br in s:
            if br in start:
                tr = tracker.open(start[br])
            else:
                tr = tracker.close(br)
            if tr is None:
                return False
        if len(tracker.tracker)!=0:
            return False
        else:
            return True

class Tracker:
    def __init__(self) -> None:
        self.tracker = []
    
    def open(self, br):
        self.tracker.append(br)
        return br
    
    def close(self, br):
        if self.tracker:
            if br == self.tracker[-1]:
                return self.tracker.pop()
            else:
                return None
        else:
            return None
    
    def __str__(self):
        return str(self.tracker)


'''
class Solution(object):
	def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in d:  # 1
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:  # 2
                return False
        return len(stack) == 0 # 3
'''
# @lc code=end

