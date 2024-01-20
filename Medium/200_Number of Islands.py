"""Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'."""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row = len(grid)
        cols = len(grid[0]) 
        islands = 0

        def change(r,c):
            grid[r][c] = 2
            if r-1>=0 and grid[r-1][c]=="1":             #top
                change(r-1,c)
            if r+1<len(grid) and grid[r+1][c]=="1":     #bottom
                change(r+1,c)
            if c-1>=0 and grid[r][c-1]=="1":             #left
                change(r,c-1)
            if c+1<len(grid[r]) and grid[r][c+1]=="1":  #right
                change(r,c+1)


        for r in range(row):
            for c in range(cols):
                if grid[r][c]=="1":
                    change(r,c)
                    islands+=1
        
        return islands


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ],  
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
    ]

    for i, case in enumerate(test_cases, 1):
        result = sol.numIslands(case)
        print(f"Test Case {i}: Number of Islands = {result}")