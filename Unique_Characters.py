
"""
Unique Characters in String
Problem
Given a string,determine if it is compreised of all unique characters.
For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return false.
"""

# Solution 1
def unique_characters(s):
    return len(s) == len(set(s))

# Solution 2
def unique_characters2(s):
    unique_set = set()
    for char in s:
        if char in unique_set:
            return False
        else:
            unique_set.add(char)
    return True
