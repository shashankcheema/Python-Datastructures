# coding: utf-8
"""
Balanced Parentheses Check

Problem Statement:
Given a string of opening and closing parentheses, check whether it’s balanced.
We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}.
Assume that the string doesn’t contain any other character than these, no spaces words or numbers.
As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened.
For example ‘([])’ is balanced but ‘([)]’ is not.

You can assume the input string has no spaces.
"""

def balance_check(s):
    chars = []
    mapping = {'{': '}', '[': ']', '(': ')'}

    # If String has odd number of parentheses - It will return False
    if len(s) % 2 != 0:
        return False

    for i in s:
        if i in mapping.keys():
            chars.append(i)
        else:
            if i == mapping[chars[-1]]:
                chars.pop()

    return len(chars) == 0

