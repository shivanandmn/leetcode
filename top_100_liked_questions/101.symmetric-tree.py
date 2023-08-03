#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
    
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)

        
# @lc code=end

"""
Coming up with the above approach for the "Symmetric Tree" problem, or any problem for that matter, requires a combination of problem-solving skills and understanding of data structures and algorithms. Here are some key steps and techniques that can help you intuitively solve similar problems:

**2. Analyze Examples:**
   - Take a few examples of varying complexities and try to solve them manually. Understand how symmetry works in binary trees.
   - Identify patterns and common elements in symmetric binary trees.

**3. Observe Symmetry Properties:**
   - Observe that a symmetric binary tree's left and right subtrees form symmetric pairs.
   - Understand that symmetric pairs have the same value at the corresponding positions and their subtrees are also symmetric.

**4. Recursive Property:**
   - Many tree-related problems can be solved using a recursive approach.
   - Recursive thinking often involves breaking a problem down into smaller, simpler subproblems of the same type.
   - For the "Symmetric Tree" problem, observe how the left and right subtrees exhibit the same symmetry property as the overall tree.

**5. Base Case and Recursive Step:**
   - Identify the base case(s) for the recursion, which defines when the recursion should stop.
   - Define the recursive step, where you call the same function on smaller instances of the problem.

**6. Divide and Conquer:**
   - Many tree-related problems can be solved using a divide-and-conquer approach, where you break the problem into smaller parts and solve each part separately.
   - In this case, you divide the problem into checking the symmetry of subtrees.

**7. Test Your Approach:**
   - Implement the solution and test it against the provided examples and additional test cases.
   - Debug and verify the output against your manual calculations.

**8. Generalize and Abstract:**
   - After successfully solving the problem, try to generalize the solution and identify the underlying patterns and principles.
   - Abstract the problem to a higher level, recognizing similarities to other problems.

**9. Practice and Exposure:**
   - Practice solving similar problems regularly to reinforce your skills and develop intuition.
   - Exposure to different problem types and variations will help you recognize common patterns and strategies.

**10. Learn from Others:**
   - Read and analyze solutions from other developers and compare them with your approach.
   - Discuss the problem with others and learn different approaches and techniques.

Remember that problem-solving skills develop over time with practice and exposure to various problems. Keep solving different types of problems, work on coding challenges, and study data structures and algorithms to strengthen your intuition and problem-solving abilities. As you encounter more problems and apply different techniques, you'll become more adept at solving a wide range of coding challenges. Happy coding!
"""