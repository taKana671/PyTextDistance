"""
Levenshtein distance.
The algorithm is described on:
https://en.wikipedia.org/wiki/Levenshtein_distance
"""
# cython: boundscheck = False
# cython: wraparound = False
from cpython.array cimport array, clone
from cython cimport boundscheck, wraparound
from cython.view cimport array as cvarray


cpdef int levenshtein(str s1, str s2):
    if s1 == s2:
        return 0

    return distance(s1, s2)


cpdef double normalized_levenshtein(str s1, str s2):
    if s1 == s2:
        return 0

    return <double>distance(s1, s2) / max(len(s1), len(s2))


cdef int distance(str s1, str s2):

    cdef:
        int s1_len = len(s1)
        int s2_len = len(s2)
        int i
        array template = array('q')
        long long[::1] v1, v2
        int[:, ::1] arr

    if s1_len == 0:
        return s2_len
    if s2_len == 0:
        return s1_len

    v1 = clone(template, s1_len, zero=False)
    for i in range(s1_len):
        v1[i] = hash(s1[i])
    v2 = clone(template, s2_len, zero=False)    
    for i in range(s2_len):
        v2[i] = hash(s2[i])

    arr = cvarray(shape=(s1_len+1, s2_len+1), itemsize=sizeof(int), format='i')

    return calculation(v1, v2, arr)


cdef inline int calculation(long long[::1] v1, long long[::1] v2, int[:, ::1] arr):

    cdef:
        int s1_range = arr.shape[0]
        int s2_range = arr.shape[1] 
        int i, j
        
    for i in range(s2_range):
        arr[0, i] = i
    for i in range(s1_range):
        arr[i, 0] = i

    for i in range(1, s1_range):
        for j in range(1, s2_range):
            arr[i, j] = min(
                arr[i-1, j] + 1,
                arr[i, j-1] + 1,
                arr[i-1, j-1] + (0 if v1[i-1]==v2[j-1] else 1)
            )
        
    return arr[v1.shape[0], v2.shape[0]]




