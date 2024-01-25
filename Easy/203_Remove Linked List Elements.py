"""Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        curr = head
    
        if not head:
            return head

        while head and head.val==val:
            head=head.next

        while curr.next:
            if curr.next.val==val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        
        return head

# Function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Test Cases
if __name__ == "__main__":
    sol = Solution()


    example_head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    val_to_remove = 6
    result_head = sol.removeElements(example_head, val_to_remove)
    print("Example Test Case:")
    print_linked_list(result_head)


    test_case_1 = ListNode(1, ListNode(2, ListNode(2, ListNode(4, ListNode(5)))))
    val_to_remove_1 = 2
    result_head_1 = sol.removeElements(test_case_1, val_to_remove_1)
    print("\nTest Case 1:")
    print_linked_list(result_head_1)

    test_case_2 = ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1)))))
    val_to_remove_2 = 1
    result_head_2 = sol.removeElements(test_case_2, val_to_remove_2)
    print("\nTest Case 2:")
    print_linked_list(result_head_2)
