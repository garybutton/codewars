"""
Python version: 3.4.3

Codewars URL: https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/
Kata name: Split strings

Complete the solution so that it splits the string into pairs of two characters. If the string 
contains an odd number of characters then it should replace the missing second character of the 
final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""

def solution(s):
    if s:
        split = 2
        pairs = [s[i:i+split] for i in range(0, len(s), split)]
        if len(pairs[-1]) == 1:
            pairs[-1] += '_'
    else:
        pairs = []
    return pairs
