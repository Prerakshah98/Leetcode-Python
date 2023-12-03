"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}

        for c in s:
            if c not in dic:
                dic[c]=1
            else:
                dic[c]+=1
            
        for i in t:
            if i in dic:
                dic[i]-=1
            else:
                dic[i]=1
        
        return all(values==0 for values in dic.values())
        
# Test Cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("anagram", "nagaram"),
        ("rat", "car"), 
        ("", ""),  
        ("a", "a")]

    for i, (s, t) in enumerate(test_cases, 1):
        result = sol.isAnagram(s, t)
        print(f"Test Case {i}: '{s}' and '{t}' -> Result: {result}")
        
