import sys

# @profile
def levenshtein(s1, s2):
    if s1 == s2:
        return 0
    
    s1_len = len(s1)
    s2_len = len(s2)

    if s1_len == 0:
        return s2_len
    if s2_len == 0:
        return s1_len
    
    arr = [[j for j in range(s2_len + 1)] if i == 0 \
        else [i if j == 0 else 0 for j in range(s2_len+1)] for i in range(s1_len+1)]
    
    for i in range(1, s1_len+1):
        for j in range(1, s2_len+1):
            d1 = arr[i-1][j] + 1
            d2 = arr[i][j-1] + 1
            d3 = arr[i-1][j-1] + (0 if s1[i-1]==s2[j-1] else 1)
            arr[i][j] = min(d1, d2, d3)

    return arr[s1_len][s2_len]


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 3:
        sys.exit(1)
    print(levenshtein(args[1], args[2]))

