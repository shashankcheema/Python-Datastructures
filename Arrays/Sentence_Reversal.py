"""
Sentence Reversal Problem
Given a string of words, reverse all the words. For example:

Given: 'This is the best'
Return: 'best the is This'
"""

# Solution 1 - using reversed()
def sentence_reversal(string):
    return " ".join(reversed(string.split()))

# Solution 2 - using slicing
def sentence_reversal2(string):
    return " ".join(string.split()[::-1])

# Solution 1 and 2 are good but not a good fit for interviews
# Instead of using split we can write our own code to split and store the words in a array

def sentence_reversal3(string):

    words = []
    spaces = [' ']
    i = 0

    while i < len(string):
        if string[i] not in spaces:
            word_start = i
            while i < len(string) and string[i] not in spaces:
                i += 1
            words.append(string[word_start:i])
        i += 1

    return " ".join(words[::-1])


