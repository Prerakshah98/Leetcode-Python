"""Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def solve(n1,n2):
            if n1 and n2:
                return n1.val==n2.val and solve(n1.left,n2.right) and solve(n1.right,n2.left)
            elif n1 or n2:
                return False
            return True

        return solve(root.left,root.right)


if __name__ == "__main__":
    # Test case 1: Symmetric tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)

    sol = Solution()
    assert sol.isSymmetric(root1) == True

    # Test case 2: Asymmetric tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)

    assert sol.isSymmetric(root2) == False

    print("All test cases passed successfully.")