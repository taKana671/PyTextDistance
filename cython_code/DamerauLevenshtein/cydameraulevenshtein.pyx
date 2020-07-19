"""
Damerau_Levenshtein distance
The algorithm is described on:
https://en.wikipedia.org/wiki/Damerau–Levenshtein_distance
https://www.lemoda.net/text-fuzzy/damerau-levenshtein/
"""
# cython: boundscheck = False
# cython: wraparound = False
from cython.view cimport array as cvarray


cpdef int damerau_levenshtein(str s1, str s2):
    if s1 == s2:
        return 0

    return distance(s1, s2)


cdef int distance(str s1, str s2):

    cdef:
        int s1_len = len(s1)
        int s2_len = len(s2)
        int max_dist
        int[:, ::1] arr

    if not s1_len:
        return s2_len
    if not s2_len:
        return s1_len

    arr = cvarray(shape=(s1_len + 2, s2_len + 2), itemsize=sizeof(int), format='i')
    max_dist = s1_len + s2_len
    return calculation(s1, s2, max_dist, arr)


cdef inline int calculation(str s1, str s2, int max_dist, int[:, ::1] arr):

    cdef:
        int i, j, k, l, temp, cost
        int s1_range = arr.shape[0]
        int s2_range = arr.shape[1]
        dict charas = {}

    arr[:, :] = max_dist

    for i in range(1, s1_range):
        arr[i, 1] = i - 1
    for j in range(1, s2_range):
        arr[1, j] = j - 1
    
    for i in range(2, s1_range):
        temp = 1
        for j in range(2, s2_range):
            k = charas.get(s2[j-2], 1)
            l = temp
            cost = 0 if s1[i-2] == s2[j-2] else 1
            if not cost:
                temp = j
            arr[i, j] = min(
                arr[i, j-1] + 1, # insertion
                arr[i-1, j] + 1, # deletion                        
                arr[i-1, j-1] + cost, # substitution
                # max: cost of letters between transposed letters
                # 1 addition + 1 deletion = 1 substitution, 1: cost of the transposition itself
                arr[k-1, l-1] + max((i-k-1), (j-l-1)) + 1 # transposition
                )
        charas[s1[i-2]] = i
    
    return arr[s1_range-1, s2_range-1]

