"""Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: [ListNode]) -> bool:
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False
    
# Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Linked list with a cycle
    head_with_cycle = ListNode(3)
    node1 = ListNode(2)
    node2 = ListNode(0)
    node3 = ListNode(-4)
    head_with_cycle.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node1  # creates a cycle

    result_with_cycle = sol.hasCycle(head_with_cycle)
    print(f"Test Case 1: Linked list with cycle - Result: {result_with_cycle}")

    # Test Case 2: Linked list without a cycle
    head_without_cycle = ListNode(1)
    node4 = ListNode(2)
    node5 = ListNode(3)
    node6 = ListNode(4)
    head_without_cycle.next = node4
    node4.next = node5
    node5.next = node6  # no cycle

    result_without_cycle = sol.hasCycle(head_without_cycle)
    print(f"Test Case 2: Linked list without cycle - Result: {result_without_cycle}")