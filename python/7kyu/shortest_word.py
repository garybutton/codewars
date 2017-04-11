"""
Python version: 3.4.3

Codewars URL: https://www.codewars.com/kata/shortest-word/
Kata name: Shortest word

x Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""

def find_short(s):
    string_of_words = s
    string_list = string_of_words.split()
    shortest_word = string_list[0]
    for word in string_list:
        if len(word) < len(shortest_word):
            shortest_word = word
    return len(shortest_word)
