"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if int(x)<0:
            x = int(x[0]+x[1:][::-1])
        else:
            x = int(x[::-1])

        return x if -2**31<=x<=2**31 else 0

# Test Cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        123,  
        -123,  
        120, 
        0
    ]

    for i, case in enumerate(test_cases, 1):
        result = sol.reverse(case)
        print(f"Test Case {i}: Input = {case}, Output = {result}")