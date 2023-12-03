"""Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle."""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = total_sum = nums[0]
        for i in range (1,len(nums)):
            current_sum = max(nums[i], nums[i]+current_sum)
            total_sum = max(current_sum,total_sum)
            
        return total_sum
    
# Test Cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1], 
        [5, 4, -1, 7, 8]
    ]

    for i, case in enumerate(test_cases, 1):
        result = sol.maxSubArray(case)
        print(f"Test Case {i}: Input = {case}, Maximum Subarray Sum = {result}")
