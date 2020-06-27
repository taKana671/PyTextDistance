
def levenshtein(str s1, str s2):
    
    cdef int s1_len = len(s1)
    cdef int s2_len = len(s2)
    cdef int s1_range = s1_len + 1
    cdef int s2_range = s2_len + 1 
    cdef int i, j, d1, d2, d3

    if s1 == s2:
        return 0

    if s1_len == 0:
        return s2_len
    if s2_len == 0:
        return s1_len
    
    arr = [[j for j in range(s2_range)] if i == 0 \
        else [i if j == 0 else 0 for j in range(s2_len+1)] for i in range(s1_range)]
    

    for i in range(1, s1_range):
        for j in range(1, s2_range):
            d1 = arr[i-1][j] + 1
            d2 = arr[i][j-1] + 1
            d3 = arr[i-1][j-1] + (0 if s1[i-1]==s2[j-1] else 1)
            arr[i][j] = min(d1, d2, d3)


    return arr[s1_len][s2_len]
