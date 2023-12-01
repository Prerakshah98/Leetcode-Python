"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 """
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}


        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n]=1
        print(count)

        return sorted(count, key=count.get, reverse=True)[0:k]
    
    
# Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2),
        ([1], 1)
    ]

    for i, (nums, k) in enumerate(test_cases, 1):
        result = sol.topKFrequent(nums, k)
        print(f"Test Case {i}: Input = {nums}, k = {k}, Top K Frequent Elements = {result}")