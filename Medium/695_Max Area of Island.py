"""You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        cols = len(grid[0]) 
        max_area = 0


        def change(r,c):
            grid[r][c] = 0
            area=1
            if r-1>=0 and grid[r-1][c]==1:             #top
                area += change(r-1,c)
            if r+1<len(grid) and grid[r+1][c]==1:     #bottom
                area += change(r+1,c)
            if c-1>=0 and grid[r][c-1]==1:             #left
                area += change(r,c-1)
            if c+1<len(grid[r]) and grid[r][c+1]==1:  #right
               area += change(r,c+1)
            return area


        for r in range(row):
            for c in range(cols):
                if grid[r][c]==1:
                    max_area = max(max_area, change(r,c))
                    
        return max_area


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    ]

    for i, case in enumerate(test_cases, 1):
        result = sol.maxAreaOfIsland(case)
        print(f"Test Case {i}: Max Area = {result}")