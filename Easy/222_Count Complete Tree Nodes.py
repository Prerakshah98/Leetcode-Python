"""Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# Test Cases
if __name__ == "__main__":

    tree_1 = TreeNode(1)
    tree_1.left = TreeNode(2)
    tree_1.right = TreeNode(3)
    tree_1.left.left = TreeNode(4)
    tree_1.left.right = TreeNode(5)
    tree_1.right.left = TreeNode(6)

    # Instance of Solution class
    sol = Solution()

    # Testing countNodes function

    print("Number of nodes in tree_2:", sol.countNodes(tree_1))  # Output: 6