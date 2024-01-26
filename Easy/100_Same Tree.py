"""Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104"""


# Definition for a binary tree node.
from typing import Optional

class Solution:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p==None and q==None:
            return True
        
        if p==None or q==None or p.val!=q.val:
            return False

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


if __name__ == "__main__":
    # Test cases
    sol = Solution()
    
    # Test case 1: Identical trees
    p1 = sol.TreeNode(1)
    p1.left = sol.TreeNode(2)
    p1.right = sol.TreeNode(3)
    
    q1 = sol.TreeNode(1)
    q1.left = sol.TreeNode(2)
    q1.right = sol.TreeNode(3)
    
    assert sol.isSameTree(p1, q1) == True
    
    # Test case 2: Different trees
    p2 = sol.TreeNode(1)
    p2.left = sol.TreeNode(2)
    
    q2 = sol.TreeNode(1)
    q2.right = sol.TreeNode(2)
    
    assert sol.isSameTree(p2, q2) == False