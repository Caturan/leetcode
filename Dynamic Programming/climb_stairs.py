"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

def climbStairs(n: int) -> int:
    k = [1,2,3]
    
    if n == 1 or n == 2:
        return n
    else:    
        for num in range(3,n):
            sum = 0
            k.append(k[num-1] + k[num-2])
    return k[-1]
   
print(climbStairs(n=8))

"""
3 -- 3
4 -- 5
5 --8
6 -- 13
"""