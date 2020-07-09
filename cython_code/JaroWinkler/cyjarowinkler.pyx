"""
Jaro distance
The higher the Jaro distance for two strings is, the more similar the strings are.
The score is normalized such that 0 equates to no similarity and 1 is an exact match.
The algorithm is described on:
https://en.wikipedia.org/wiki/Jaro-Winkler_distance
"""
from cpython.array cimport array, clone
from cython cimport boundscheck, wraparound, cdivision


@boundscheck(False)
@wraparound(False)
cpdef double jaro(str s1, str s2, bint winkler=False):

    if s1 == s2:
        return 1.0

    cdef:
        int len_s1 = len(s1)
        int len_s2 = len(s2)
        int match, trans
        double jaro_distance
        # array template = array('i')
        array template
        int[::1] match_s1, match_s2
    
    if len_s1 == 0 or len_s2 == 0:
        return 0.0

    # make len_s1 always shorter (or equall to len_s2)
    if len_s1 > len_s2:
        s1, s2 = s2, s1
        len_s1, len_s2 = len_s2, len_s1
    
    template = array('i')
    match_s1 = clone(template, len_s1, zero=True)
    match_s2 = clone(template, len_s2, zero=True)
    jaro_distance = distance(s1, len_s1, match_s1, s2, len_s2, match_s2)

    if winkler:
        jaro_distance = jaro_winkler(s1, s2, len_s1, jaro_distance)

    return jaro_distance


@cdivision(True)
@boundscheck(False)
@wraparound(False)
cdef inline double distance(str s1, int len_s1, int[::1] match_s1, 
        str s2, int len_s2, int[::1] match_s2):

    cdef:
        int search_range
        int match
        int i, j, k, start, end, trans
        # int[::1] match_s1 = array('i', [0] * len_s1)
        # int[::1] match_s2 = array('i', [0] * len_s2)

    # Maxumum distance upto which matching is allowed
    search_range = (len_s1 + 1) // 2
    # search_range = floor(max(len_s1, len_s2) / 2) - 1
  
    match = 0
   
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
        return 0

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

    return (<double>match / len_s1 + <double>match / len_s2 + <double>(match - trans) / match) / 3.0


@boundscheck(False)
@wraparound(False)
cdef inline double jaro_winkler(str s1, str s2, int search_range, double jaro_distance):
    cdef:
        int prefix
        int i
    
    # If the jaro_distance is above a threshold
    if jaro_distance > 0.7:
        prefix = 0
        for i in range(search_range):
            if s1[i] == s2[i]:
                prefix += 1
            else:
                break
        prefix = min(4, prefix)
        jaro_distance += 0.1 * prefix * (1 - jaro_distance)

    return jaro_distance





   
