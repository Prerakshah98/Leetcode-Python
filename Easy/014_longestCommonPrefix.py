"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        smallest = min(strs)
        largest = max(strs)

        for i,v in enumerate(smallest):
            if v != largest[i]:
                return smallest[:i]
        return smallest

# Test Cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ["flower", "flow", "flight"],  # Example test case 1
        ["dog", "racecar", "car"],    # Example test case 2
        ["hello", "hey", "hi"],       # No common prefix
        ["abc", "abcd", "abcde"],     # Common prefix is "abc"
    ]

    for i, case in enumerate(test_cases, 1):
        result = sol.longestCommonPrefix(case)
        print(f"Test Case {i}: Input = {case}, Longest Common Prefix = {result}")