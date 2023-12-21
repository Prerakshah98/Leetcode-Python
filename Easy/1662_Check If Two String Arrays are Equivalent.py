"""Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

 

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
 

Constraints:

1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters."""


from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # w1=""
        # w2=""

        # for w in word1:
        #     w1+=w
        
        # for w in word2:
        #     w2+=w
        
        # return w1==w2
        return "".join(word1)=="".join(word2)
    


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (["ab", "c"], ["a", "bc"]),  
        (["a", "cb"], ["ab", "c"]),  
        (["abc", "d", "defg"], ["abcddefg"])
    ]

    for i, (w1, w2) in enumerate(test_cases, 1):
        result = sol.arrayStringsAreEqual(w1, w2)
        print(f"Test Case {i}: Word1 = {w1}, Word2 = {w2}, Result = {result}")