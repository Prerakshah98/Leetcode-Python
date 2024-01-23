"""Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces."""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charSet=set()
        # result = 0

        # l = 0
        
        # for r in range(len(s)):
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l+=1
        #     charSet.add(s[r])
        #     result = max(result, r-l+1)
        # return result                                

        seen = ''
        res = 0

        for c in s:
            if c not in seen:
                seen += c
            else:
                seen = seen[seen.index(c)+1:] + c
                
            res = max(res,len(seen))
        return res

# Test Cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        "abcabcbb", 
        "bbbbb",    
        "pwwkew",   
        "dvdf"
    ]

    for i, case in enumerate(test_cases, 1):
        result = sol.lengthOfLongestSubstring(case)
        print(f"Test Case {i}: Input = {case}, Longest Substring Length = {result}")