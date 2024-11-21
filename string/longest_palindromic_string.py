"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""
s = "cbbd"
n = len(s)
max = '' 
for i in range(n):
    for j in range(i+1,n+1):
        sub = s[i:j]
        if sub == sub[::-1]:
            if len(sub) > len(max):
                max = sub  

print(max)