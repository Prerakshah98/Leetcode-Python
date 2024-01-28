"""Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        
        
# Test Cases
if __name__ == "__main__":
    # Example binary tree
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    example_tree = TreeNode(1)
    example_tree.left = TreeNode(2)
    example_tree.right = TreeNode(3)
    example_tree.left.left = TreeNode(4)
    example_tree.left.right = TreeNode(5)

    sol = Solution()

    print("Example Tree Preorder Traversal:", sol.preorderTraversal(example_tree))