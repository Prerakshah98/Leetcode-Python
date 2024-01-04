"""Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 

Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 

Constraints:

The input must be a binary string of length 32
 

Follow up: If this function is called many times, how would you optimize it?"""

class Solution:
    def reverseBits(self, n: int) -> int:
        output=0

        for _ in range(0,32):
            output <<= 1
            if n&1 == 1:
                output+=1
            n >>= 1

        return output 
    

# Test Cases
if __name__ == "__main__":
    sol = Solution()

    input_1 = int('00000010100101000001111010011100', 2)
    # Expected Output: 964176192 (binary: 00111001011110000010100101000000)
    result_1 = sol.reverseBits(input_1)
    print(f"Test Case 1: Input = {input_1}, Reversed Bits = {result_1}")

    input_2 = int('11111111111111111111111111111101', 2)
    # Expected Output: 3221225471 (binary: 10111111111111111111111111111111)
    result_2 = sol.reverseBits(input_2)
    print(f"Test Case 2: Input = {input_2}, Reversed Bits = {result_2}")
