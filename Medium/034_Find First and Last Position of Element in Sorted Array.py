"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first,last = 0, len(nums)-1

        while first<=last:
            if nums[first]<target:
                first+=1
            elif nums[last]>target:
                last-=1
            elif nums[first]==nums[last]==target:
                return [first,last]
        return [-1,-1]


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8),  
        ([5, 7, 7, 8, 8, 10], 6),  
        ([], 0)
    ]

    for i, (nums, target) in enumerate(test_cases, 1):
        result = sol.searchRange(nums, target)
        print(f"Test Case {i}: nums={nums}, target={target}, Range={result}")