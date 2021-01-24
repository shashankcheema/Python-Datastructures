"""
Problem
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"

"""

def anagram(s,t):
    # Remove the spaces and Convert them to lowercase
    s = s.replace(' ', '').lower()
    t = t.replace(' ', '').lower()

    counter = {}

    for character in s:
        if character in counter:
            counter[character] += 1
        else:
            counter[character] = 1

    for character in t:
        if character in counter:
            counter[character] -= 1
        else:
            counter[character] = 1

    for value in counter:
        if counter[value] != 0:
            return False

    return True
