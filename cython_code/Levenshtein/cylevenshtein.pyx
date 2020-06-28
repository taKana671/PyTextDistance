from cython.view cimport array
from cython import boundscheck, wraparound


def levenshtein(str s1, str s2)
    return distance(tuple(s1), tuple(s2))


@boundscheck(False)
@wraparound(False)
cdef int distance(tuple s1, tuple s2):

    cdef int s1_len = len(s1)
    cdef int s2_len = len(s2)
    cdef int s1_range = s1_len + 1
    cdef int s2_range = s2_len + 1 
    cdef int i, j
    cdef int[:, ::1] arr
    cdef str word
    
    if s1 == s2:
        return 0

    if s1_len == 0:
        return s2_len
    if s2_len == 0:
        return s1_len

    arr = array(shape=(s1_range, s2_range), itemsize=sizeof(int), format='i')
    for i in range(s2_range):
        arr[0, i] = i
    
    for i in range(s1_range):
        arr[i, 0] = i
 
    for i in range(1, s1_range):
        word = s1[i-1]
        for j in range(1, s2_range):
            arr[i, j] = min(
                arr[i-1, j] + 1,
                arr[i, j-1] + 1,
                arr[i-1, j-1] + (0 if word==s2[j-1] else 1)
            )
          
    return arr[s1_len, s2_len]



