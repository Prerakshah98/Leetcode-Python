"""Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

 

Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
 

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1."""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans=0
        inc = 0

        while head:
            ans = ans*2 + head.val
            head=head.next
            inc+=1
        
        return ans

# Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Binary: 101, Decimal: 5
    list_1 = ListNode(1)
    list_1.next = ListNode(0)
    list_1.next.next = ListNode(1)
    result_1 = sol.getDecimalValue(list_1)
    print(f"Test Case 1: Binary: 101, Decimal: {result_1}")

    # Test Case 2: Binary: 1101, Decimal: 13
    list_2 = ListNode(1)
    list_2.next = ListNode(1)
    list_2.next.next = ListNode(0)
    list_2.next.next.next = ListNode(1)
    result_2 = sol.getDecimalValue(list_2)
    print(f"Test Case 2: Binary: 1101, Decimal: {result_2}")

    # Test Case 3: Binary: 111, Decimal: 7
    list_3 = ListNode(1)
    list_3.next = ListNode(1)
    list_3.next.next = ListNode(1)
    result_3 = sol.getDecimalValue(list_3)
    print(f"Test Case 3: Binary: 111, Decimal: {result_3}")