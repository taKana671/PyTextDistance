"""
Hamming distance
The algorithm is described on:
https://en.wikipedia.org/wiki/Hamming_distance
"""
from cython cimport boundscheck, wraparound


@boundscheck(False)
@wraparound(False)
cpdef int hamming(str s1, str s2) except -1:

    cdef:
        int len_s1 = len(s1)
        int len_s2 = len(s2)
        int i, count = 0

    if len_s1 != len_s2:
        raise ValueError('expected two strings of the same length')

    for i in range(len_s1):
        if s1[i] != s2[i]:
            count += 1
    return count
    
    