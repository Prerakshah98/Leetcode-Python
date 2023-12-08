"""Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=0
        r=len(s)-1

        while l<r:
            s[l],s[r] = s[r],s[l]
            l+=1
            r-=1
            
def test_reverse_string():
    sol = Solution()

    input_1 = ["h", "e", "l", "l", "o"]
    expected_1 = ["o", "l", "l", "e", "h"]
    sol.reverseString(input_1)
    assert input_1 == expected_1, f"Test Case 1 Failed: Expected {expected_1}, Got {input_1}"

    input_2 = ["H", "a", "n", "n", "a", "h"]
    expected_2 = ["h", "a", "n", "n", "a", "H"]
    sol.reverseString(input_2)
    assert input_2 == expected_2, f"Test Case 2 Failed: Expected {expected_2}, Got {input_2}"
    print("All test cases passed!")

if __name__ == "__main__":
    test_reverse_string()