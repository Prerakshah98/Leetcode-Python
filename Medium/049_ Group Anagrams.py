"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            sort = ''.join(sorted(s))
            if sort in dic:
                dic[sort].append(s)
            else:
                dic[sort]=[s]        
        return dic.values()
    
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],  # Example test case 1
        [""],  
        ["a"],  
    ]

    for i, case in enumerate(test_cases, 1):
        result = sol.groupAnagrams(case)
        print(f"Test Case {i}: Input = {case}, Grouped Anagrams = {list(result)}")