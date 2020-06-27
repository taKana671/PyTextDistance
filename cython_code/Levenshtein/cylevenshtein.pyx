from cython import boundscheck, wraparound
import numpy as np


@boundscheck(False)
@wraparound(False)
def levenshtein(str s1, str s2):
    
    cdef int s1_len = len(s1)
    cdef int s2_len = len(s2)
    cdef int s1_range = s1_len + 1
    cdef int s2_range = s2_len + 1 
    cdef int i, j, d1, d2, d3
    cdef int[:, ::1] arr
    
    arr = np.zeros((s1_range, s2_range), dtype=np.int32)
    
    if s1 == s2:
        return 0

    if s1_len == 0:
        return s2_len
    if s2_len == 0:
        return s1_len

    for i in range(s2_range):
        arr[0, i] = i
    
    for i in range(s1_range):
        arr[i, 0] = i

    
    for i in range(1, s1_range):
        for j in range(1, s2_range):
            d1 = arr[i-1, j] + 1
            d2 = arr[i, j-1] + 1
            d3 = arr[i-1, j-1] + (0 if s1[i-1]==s2[j-1] else 1)
            arr[i, j] = min(d1, d2, d3)


    return arr[s1_len, s2_len]



