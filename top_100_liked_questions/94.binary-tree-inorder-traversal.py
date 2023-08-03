#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recursively(node):
            if node is None:
                return []
            else:
                left = recursively(node.left)
                cur = [node.val]
                right = recursively(node.right)
                return left + cur + right
        return recursively(root) 

        
# @lc code=end

"""
Sure! Let's explore the iterative approach for performing an inorder traversal of a binary tree using a stack.

**Iterative Approach (Using Stack):**
In the iterative approach, we use a stack data structure to simulate the recursive function call stack. Instead of using the function call stack for recursion, we manually manage a stack to keep track of the nodes we need to process.

Here's a step-by-step explanation of the iterative inorder traversal algorithm:

1. **Initialize Stack:**
   - Create an empty stack to store nodes that need to be processed.

2. **Traverse Left Subtree:**
   - Starting from the root node, keep traversing to the left child of each node and push each node onto the stack while doing so.
   - This process continues until we reach the leftmost leaf node.

3. **Process Nodes:**
   - Pop the top node from the stack and process its value.
   - Move to the right child of the popped node, if it exists, and repeat steps 2 and 3 to traverse the right subtree.

4. **Repeat Until Stack is Empty:**
   - Keep repeating steps 2 and 3 until the stack becomes empty.
   - When the stack is empty, we have traversed the entire binary tree.

Let's implement the iterative approach in Python:

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    result = []       # To store the inorder traversal
    stack = []        # Stack to keep track of nodes

    current = root    # Start from the root node

    while current or stack:
        # Traverse to the leftmost node and push each node onto the stack
        while current:
            stack.append(current)
            current = current.left

        # Pop the top node from the stack and process its value
        current = stack.pop()
        result.append(current.val)

        # Move to the right child and repeat the process for the right subtree
        current = current.right

    return result
```

**Example Usage:**
Consider the binary tree from the earlier example:

```
        5
       / \
      3   7
     / \ / \
    2  4 6  8
```

To get the inorder traversal, we call the function with the root of the tree:

```python
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

result = inorderTraversal(root)
print(result)
```

Output:
```
[2, 3, 4, 5, 6, 7, 8]
```

As you can see, the `inorderTraversal` function using the iterative approach produces the same result as the recursive approach. The iterative approach avoids the function call overhead of recursion and uses a stack to efficiently process the nodes in the desired order.
"""


"""REmeber and REvise

Great question! Here are the key takeaways from the "Binary Tree Inorder Traversal" problem that you can remember and revise for future reference:

1. **Inorder Traversal**:
   - Inorder traversal is a way to visit all the nodes of a binary tree in a specific order: left subtree, current node, right subtree.
   - It gives you the elements of the binary tree in ascending order if the tree stores elements in sorted order.

2. **Recursive Approach**:
   - The recursive approach involves defining a recursive function that performs the inorder traversal.
   - The function follows the order: left subtree, current node, right subtree.
   - It uses a base case to terminate recursion when a node is `None`.
   - Recursive solutions are generally intuitive but may lead to function call overhead for large trees.

3. **Iterative Approach (Using Stack)**:
   - The iterative approach simulates recursion using a stack to manage the nodes to be processed.
   - It starts by traversing to the leftmost node while pushing nodes onto the stack.
   - Then, it processes nodes by popping them from the stack and visiting their values.
   - It then moves to the right child and repeats the process for the right subtree.
   - Iterative solutions are often more space-efficient compared to recursion.

4. **Choice of Approach**:
   - Both approaches yield the same result, but the iterative approach can be more efficient in terms of space complexity.
   - Recursive approach may be simpler to implement, while iterative approach requires manual stack management.

5. **Implementing Binary Trees**:
   - Understanding the representation of binary trees is crucial. Here, the `TreeNode` class is commonly used.
   - Each `TreeNode` object stores a value, a left child, and a right child (or `None` if there's no child).

6. **Edge Cases**:
   - Always handle edge cases such as an empty tree (root is `None`) or a tree with only one node.

7. **Practice and Reinforcement**:
   - Practice implementing both approaches to gain confidence in solving tree traversal problems.
   - Reinforce the concepts by working with various binary trees and comparing your outputs.

Remember, practice is the key to becoming proficient in solving tree traversal problems and mastering data structures and algorithms in general. By understanding and revisiting these key takeaways, you'll be better equipped to tackle similar problems in the future. Happy coding!

"""