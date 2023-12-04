"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters."""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ''.join(i for i in s if i.isalnum()).lower()
        return clean_str==clean_str[::-1]
    
# Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    test_case_1 = "A man, a plan, a canal, Panama"
    print(f"Test Case 1: {test_case_1} -> Result: {sol.isPalindrome(test_case_1)}")

    test_case_2 = "race a car"
    print(f"Test Case 2: {test_case_2} -> Result: {sol.isPalindrome(test_case_2)}")

    test_case_3 = ""
    print(f"Test Case 3: {test_case_3} -> Result: {sol.isPalindrome(test_case_3)}")
