"""
Jaro distance
The higher the Jaro distance for two strings is, the more similar the strings are.
The score is normalized such that 0 equates to no similarity and 1 is an exact match.
The algorithm is described on:
https://en.wikipedia.org/wiki/Jaro-Winkler_distance
"""
# from math import floor, ceil
# import sys


def jaro(s1, s2):

    if s1 == s2:
        return 1.0

    len_s1 = len(s1)
    len_s2 = len(s2)
    
    if len_s1 == 0 or len_s2 == 0:
        return 0.0
    # make len_s1 always shorter (or equall to len_s2)
    if len_s1 > len_s2:
        s1, s2 = s2, s1
        len_s1, len_s2 = len_s2, len_s1

    # Maxumum distance upto which matching is allowed
    search_range = (len_s1 + 1) // 2
    # search_range = floor(max(len_s1, len_s2) / 2) - 1
  
    match = 0
    match_s1 = [0] * len_s1
    match_s2 = [0] * len_s2
    # Check if there is any matches
    for i in range(len_s1):
        start = max(0, i - search_range)
        end = min(len_s2, i + search_range + 1)
        for j in range(start, end):
            if s1[i] == s2[j] and match_s2[j] == 0:
                match_s1[i] = 1
                match_s2[j] = 1
                match += 1
                break

    if not match:
        return 0.0
    
    # Number of transpositions
    trans = k = 0
    for i in range(len_s1):
        if match_s1[i]:
            while match_s2[k] == 0:
                k += 1
            if s1[i] != s2[k]:
                k += 1
                trans += 1
            else:
                k += 1
    
    trans = trans // 2
    # trans /= 2

    return ((match / len_s1 + match / len_s2 + (match - trans) / match ) / 3.0)


def jaro_winkler(s1, s2):
    jaro_distance = jaro(s1, s2)

    # If the jaro_distance is above a threshold
    if jaro_distance > 0.7:
        prefix = 0
        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                prefix += 1
            else:
                break
        prefix = min(4, prefix)
        jaro_distance += 0.1 * prefix * (1 - jaro_distance)

    return jaro_distance


if __name__ == '__main__':
    # args = sys.argv
    # if len(args) < 3:
    #     sys.exit(1)
    print(jaro('abc', 'bac'), jaro_winkler('abc', 'bac'))
    print(jaro('dicksonx', 'dixon'), jaro_winkler('dicksonx', 'dixon'))
    print(jaro('dixon', 'dicksonx'), jaro_winkler('dixon', 'dicksonx'))
    print(jaro('Brian', 'Jesus'), jaro_winkler('Brian', 'Jesus'))
    print(jaro('Thorkel', 'Thorgier'), jaro_winkler('Thorkel', 'Thorgier'))
    print(jaro('Dinsdale', 'D'), jaro_winkler('Dinsdale', 'D'))
    print(jaro('Carol','elephant'), jaro_winkler('Carol','elephant'))
    print(jaro('abcdefg', 'acbdefg'), jaro_winkler('abcdefg', 'acbdefg'))
    print(jaro('abcdefg', 'acbd'), jaro_winkler('abcdefg', 'acbd'))
    print(jaro('abcd', 'cadb'), jaro_winkler('abcd', 'cadb')) 


   
