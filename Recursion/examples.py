"""
Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer
"""

def cumulative_sum(n):
    if n == 0:
        return 0
    else:
        return n + cumulative_sum(n - 1)

"""
Given an integer, create a function which returns the sum of all the individual digits in that integer
"""

def sum_func(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_func(int(n/10))

"""
Create a function called word_split() which takes in a string phrase and a set list_of_words. 
The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. 
You can assume the phrase will only contain words found in the dictionary if it is completely splittable.

Example:
word_split('themanran',['the','ran','man'])
o/p: ['the', 'man', 'ran']
"""

def word_split(phrase,list_of_words, output = None):
    if output is None:
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)

    return output
