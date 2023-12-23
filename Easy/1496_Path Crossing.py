"""Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 

Example 1:


Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.
Example 2:


Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
 

Constraints:

1 <= path.length <= 104
path[i] is either 'N', 'S', 'E', or 'W'."""

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y=0,0

        visited= {(0,0)}

        for dir in path:
            if dir=='E':
                x+=1
            elif dir=='W':
                x-=1
        
            if dir=='N':
                y+=1
            elif dir=='S':
                y-=1
            else:
                0
            if (x,y) in visited:
                return True
            else:
                visited.add((x,y))
        
        return False
sol = Solution()

# Test cases
test_cases = [
    "NES",  
    "NESWW"
]

for idx, path in enumerate(test_cases, 1):
    result = sol.isPathCrossing(path)
    print(f"Test Case {idx}: Path = {path}, Output = {result}")