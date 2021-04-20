# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:05:42 2021
source :
    https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
    https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
@author: Bruno
"""


def user_input():
    mot = input("entrer un mot avec des lettres minuscules sans accent: ")
    for c in mot:
        if ord('a') <= ord(c) and ord(c) <= ord('z'):
            pass
        else:
            return False
    return mot


def next_word(word):
    length = len(word)
    # convert to integer
    l_int = [ord(c) for c in word]

    # from the left
    i = length - 1
    while i > 0 and l_int[i-1] > l_int[i]:
        i -= 1
    if i == 0:
        return word  # nothing to swap

    # from the left
    j = length - 1
    while l_int[j] < l_int[i-1]:
        j -= 1

    # swap
    l_int[i-1], l_int[j] = l_int[j], l_int[i-1]

    # reverse order
    l_int[i:] = l_int[length - 1: i-1: -1]

    # convert back to char
    l_c = [chr(n) for n in l_int]

    return "".join(l_c)


mot = user_input()
if mot == False:
    print("invalid word!")
else:
    print(mot, "becomes", next_word(mot))

mot = "abcde"
print(mot, "becomes", next_word(mot))

mot = "hegf"
print(mot, "becomes", next_word(mot))

mot = "fed"
print(mot, "becomes", next_word(mot))
