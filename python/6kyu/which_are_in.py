"""
Python version: 3.4.3

Codewars URL: https://www.codewars.com/kata/550554fd08b86f84fe000a58
Kata name: Which are in

Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the 
strings of a1 which are substrings of strings of a2.

Example 1:

a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

Example 2:

a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []

Notes:

Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.

Beware: r must be without duplicates.
"""

def in_array(array1, array2):
    common_elements = []
    for string in array1:
        for s in array2:
            if string in s and string not in common_elements:
                common_elements.append(string)
    return sorted(common_elements)
