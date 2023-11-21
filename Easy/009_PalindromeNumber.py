"""
Given an integer x, return true if x is a 
palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>0:
            rev = []
            temp = x
            while temp>0:
                digit = temp%10
                rev.append(digit)
                temp=temp//10
            return rev == rev[::-1]
        elif x<0:
            return False
        else:
            return True

# Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        121,  # Palindrome number
        -121,  # Negative number (not a palindrome)
        10,  # Not a palindrome
        0,  # Palindrome (single digit)
        12321,  # Palindrome number
    ]

    for i, case in enumerate(test_cases, 1):
        result = sol.isPalindrome(case)
        print(f"Test Case {i}: Number = {case}, Is Palindrome = {result}")