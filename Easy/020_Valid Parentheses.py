"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        arr = []

        for c in s:
            if(c=='(' or c=='[' or c=='{'):
                arr.append(c)
                continue
            if len(arr)==0:
                return False
            
            if ((c==")" and arr[-1]=='(') or (c=="]" and arr[-1]=='[') or (c=="}" and arr[-1]=='{')):
                del arr[-1]
            else:
                return False

        if len(arr)==0:
            return True
        else:
            return False
        
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        "()",              # Valid test case 1
        "()[]{}",          # Valid test case 2
        "(]",              # Invalid test case 3
        "([)]",            # Invalid test case 4
        "{[]}",            # Valid test case 5
        "",                # Empty string
        "((()))",          # Valid test case 6
        "{{{{{{",          # Invalid test case 7
    ]

    for i, case in enumerate(test_cases, 1):
        result = sol.isValid(case)
        print(f"Test Case {i}: Input = '{case}', Result = {result}")