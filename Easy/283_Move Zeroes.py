"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         nums[i],nums[j] = nums[j],nums[i]
        #         j+=1
        
        # return nums


        for i in range(len(nums))[::-1]:
            if nums[i]==0:
                nums.remove(0)
                nums.append(0)
            
        return nums
    

# Test Cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [0, 1, 0, 3, 12], 
        [0, 0, 0, 0, 0],  
        [1, 2, 3, 4, 5],  
        [1, 0, 2, 0, 3, 0, 4, 0]  
    ]

    for i, case in enumerate(test_cases, 1):
        sol.moveZeroes(case)
        print(f"Test Case {i}: {case}")