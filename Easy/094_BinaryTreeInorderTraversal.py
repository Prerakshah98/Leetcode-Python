"""Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root:TreeNode):
        if root is None: 
            return []
        else: 
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
# Test Cases
if __name__ == "__main__":
    # Creating a tree
    # Example Tree: 
    #       1
    #        \
    #         2
    #        /
    #       3
    # In-order traversal sequence should be [1, 3, 2]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    sol = Solution()
    result = sol.inorderTraversal(root)
    print("In-order Traversal:", result)