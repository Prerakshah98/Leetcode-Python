"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        ans = node = ListNode(0)
        
        while l1 and l2:
            if l1.val<=l2.val:
                ans.next=l1
                l1=l1.next
            else:
                ans.next=l2
                l2=l2.next
            ans=ans.next
        
        if l1:
            ans.next=l1
        else:
            ans.next=l2
        
        return node.next
    
# Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Merge two sorted lists
    l1 = ListNode(1, ListNode(3, ListNode(5)))
    l2 = ListNode(2, ListNode(4, ListNode(6)))
    merged_list = sol.mergeTwoLists(l1, l2)
    # Expected output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    while merged_list:
        print(merged_list.val, end=" -> ")
        merged_list = merged_list.next
    print("None")

    # Test Case 2: Empty lists
    l3 = None
    l4 = None
    merged_list_2 = sol.mergeTwoLists(l3, l4)
    # Expected output: None (Empty list)
    print(merged_list_2)
