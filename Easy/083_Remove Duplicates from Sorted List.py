"""83. Remove Duplicates from Sorted List
Solved
Easy
Topics
Companies
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order."""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head

        curr = head

        while curr.next:
            if curr.val==curr.next.val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        
        return head
    
# Function to print the linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: No duplicates
    head1 = ListNode(1, ListNode(1, ListNode(2)))
    result1 = sol.deleteDuplicates(head1)
    print("Test Case 1:")
    print_linked_list(result1)

    # Test Case 2: Duplicates in the middle
    head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    result2 = sol.deleteDuplicates(head2)
    print("\nTest Case 2:")
    print_linked_list(result2)

    # Test Case 3: Duplicates at the beginning
    head3 = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
    result3 = sol.deleteDuplicates(head3)
    print("\nTest Case 3:")
    print_linked_list(result3)

    # Test Case 4: Empty list
    head4 = None
    result4 = sol.deleteDuplicates(head4)
    print("\nTest Case 4:")
    print_linked_list(result4)