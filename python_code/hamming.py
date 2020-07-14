"""
Hamming distance
The algorithm is described on:
https://en.wikipedia.org/wiki/Hamming_distance
"""
def hamming(s1, s2):
    if len(s1) != len(s2):
        raise ValueError('expected two strings of the same length')
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count
    