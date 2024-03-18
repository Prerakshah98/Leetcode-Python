"""Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1."""

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxCount=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                maxCount = max(count,maxCount)
                count=0
        maxCount = max(count,maxCount)
        return maxCount


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 1, 0, 1, 1, 1],  
        [1, 0, 1, 1, 0, 1]
    ]

    for i, case in enumerate(test_cases, 1):
        result = sol.findMaxConsecutiveOnes(case)
        print(f"Test Case {i}: Input = {case}, Maximum Consecutive Ones = {result}")