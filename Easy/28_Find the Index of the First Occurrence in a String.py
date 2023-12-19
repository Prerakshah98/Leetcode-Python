"""Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters."""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


if __name__ == "__main__":
    sol = Solution()

    # Test Cases
    test_cases = [
        ("sadbutsad", "sad"),  
        ("leetcode", "leeto"), 
        ("", "")
    ]

    for i, (haystack, needle) in enumerate(test_cases, 1):
        result = sol.strStr(haystack, needle)
        print(f"Test Case {i}: haystack='{haystack}', needle='{needle}' => Result: {result}")