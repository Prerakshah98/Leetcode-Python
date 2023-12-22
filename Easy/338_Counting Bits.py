"""Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(0,n+1):
            b=bin(i)
            ans.append(b.count('1'))
        return ans
    

# Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: n = 2
    input_1 = 2
    output_1 = sol.countBits(input_1)
    print(f"Input: {input_1}, Output: {output_1}") 
    
    # Test Case 2: n = 5
    input_2 = 5
    output_2 = sol.countBits(input_2)
    print(f"Input: {input_2}, Output: {output_2}") 