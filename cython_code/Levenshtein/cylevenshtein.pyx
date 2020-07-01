"""
A Cython extension to calculate levenshtein distance.
"""

from cython import boundscheck, wraparound
from cython.view cimport array


@boundscheck(False)
@wraparound(False)
cpdef int levenshtein(str s1, str s2):
    if s1 == s2:
        return 0

    return distance(s1, s2)


@boundscheck(False)
@wraparound(False)
cdef int distance(str s1, str s2):

    cdef:
        str s
        size_t s1_len = len(s1)
        size_t s2_len = len(s2)
        size_t i
        long long[::1] v1
        long long[::1] v2
        
    if s1_len == 0:
        return s2_len
    if s2_len == 0:
        return s1_len

    v1 = array(shape=(s1_len,), itemsize=sizeof(long long int), format='q')
    v2 = array(shape=(s2_len,), itemsize=sizeof(long long int), format='q')
    for i, s in enumerate(s1):
        v1[i] = hash(s)
    for i, s in enumerate(s2):
        v2[i] = hash(s)

    return calculation(v1, v2)


@boundscheck(False)
@wraparound(False)
cdef inline int calculation(long long[::] v1, long long[::] v2):

    cdef:
        size_t s1_range = v1.shape[0] + 1
        size_t s2_range = v2.shape[0] + 1 
        size_t i, j
        cdef int[:, ::1] arr
    
    arr = array(shape=(s1_range, s2_range), itemsize=sizeof(int), format='i')
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



