"""Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address."""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        # Solution 1
        #return address.replace(".","[.]")
        
        # Solution 2
        #ans = "[.]".join(address.split("."))
        #return ans

        # Solution 3
        ans = ""

        for c in address:
            if c == ".":
                ans+="[.]"
            else:
                ans+=c
        
        return ans
    

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        "1.1.1.1",
        "255.100.50.0"
    ]

    for i, case in enumerate(test_cases, 1):
        result = sol.defangIPaddr(case)
        print(f"Test Case {i}: Original = {case}, Defanged = {result}")