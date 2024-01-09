"""Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        
        curr, prev = head, None

        while curr:
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Helper function to create a linked list from a list
    def create_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for value in arr[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    # Helper function to print a linked list
    def print_linked_list(head):
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    # Test cases
    test_cases = [
        [1, 2, 3, 4, 5], 
        [1,2],   
        []
    ]

    for i, test in enumerate(test_cases, 1):
        linked_list = create_linked_list(test)
        print(f"Test Case {i}: Input:", end=" ")
        print_linked_list(linked_list)

        reversed_list = sol.reverseList(linked_list)
        print("Reversed:", end=" ")
        print_linked_list(reversed_list)
        print()