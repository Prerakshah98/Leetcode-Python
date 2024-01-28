"""Given a binary tree, determine if it is 
height-balanced

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True,0]
            
            left = dfs(root.left)
            right= dfs(root.right)

            b = left[0] and right[0] and abs(left[1]-right[1])<=1
            return [b, 1+max(left[1],right[1])]
        
        return dfs(root)[0]



# Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Balanced tree
    root_balanced = TreeNode(1)
    root_balanced.left = TreeNode(2)
    root_balanced.right = TreeNode(3)
    root_balanced.left.left = TreeNode(4)
    root_balanced.left.right = TreeNode(5)
    root_balanced.right.right = TreeNode(6)
    balanced_result = sol.isBalanced(root_balanced)
    print("Test Case 1 (Balanced Tree):", balanced_result)

    # Test Case 2: Unbalanced tree
    root_unbalanced = TreeNode(1)
    root_unbalanced.left = TreeNode(2)
    root_unbalanced.right = TreeNode(3)
    root_unbalanced.left.left = TreeNode(4)
    root_unbalanced.left.left.left = TreeNode(5)
    unbalanced_result = sol.isBalanced(root_unbalanced)
    print("Test Case 2 (Unbalanced Tree):", unbalanced_result)