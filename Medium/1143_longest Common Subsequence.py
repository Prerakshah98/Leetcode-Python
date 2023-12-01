"""Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters."""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1,l2 = len(text1), len(text2)
        dp = [[0] * (l2+1) for _ in range(l1+1)]

        
        for i in range (1,l1+1):
            for j in range (1,l2+1):
                if(text1[i-1]==text2[j-1]):
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])

        return dp[l1][l2]
    
# Test Cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("abcde", "ace"),  
        ("abc", "def"),    
        ("abc", "abc"),
    ]
    for i, (text1, text2) in enumerate(test_cases, 1):
        result = sol.longestCommonSubsequence(text1, text2)
        print(f"Test Case {i}: Text1 = '{text1}', Text2 = '{text2}', LCS Length = {result}")