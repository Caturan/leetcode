def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = ""
        n = len(s)

        for i in range(n):
            for j in range(i+1, n+1):
                substring = s[i:j]
            
                if len(set(substring)) == len(substring):
                    if len(substring) > len(longest_substring):
                        longest_substring = substring 

        return len(longest_substring)
"""
A more optimal solution for finding the longest substring with uniquee characters can be achieved with sliding window technique, 
which reduces the time complexity to O(n) by avoiding redundant checks. 
"""


def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        start = 0
        max_length = 0 

        for end in  range(len(s)):
            current_char = s[end]

            if current_char in char_index and char_index[current_char] >= start:
                start = char_index[current_char] + 1
            
            char_index[current_char] = end 

            max_length = max(max_length, end - start + 1)

        return max_length

"""
The sliding window techniqu is a powerful approach to solve problems involving contiguous subarrays or substrings. 

Key Idea of Sliding Window: 
In a sliding window approach:
    1. We use two pointers(start abd end) to represent the beginning and end of the "window". 
    2. The window "slides" along the string to check for the desired property-in this case, a substring without repeating characters. 
"""