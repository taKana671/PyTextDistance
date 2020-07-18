"""
Damerau_Levenshtein distance
The algorithm is described on:
https://en.wikipedia.org/wiki/Damerau–Levenshtein_distance
https://www.lemoda.net/text-fuzzy/damerau-levenshtein/
"""

def damerau_levenshtein(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    max_dist = len_s1 + len_s2
    charas = {}
    arr = [[max_dist for _ in range(len_s2 + 2)] for _ in range(len_s1 + 2)]

    for i in range(1, len_s1 + 2):
        arr[i][1] = i - 1
    for j in range(1, len_s2 + 2):
        arr[1][j] = j - 1
    
    for i in range(2, len_s1 + 2):
        temp = 1
        for j in range(2, len_s2 + 2):
            k = charas.get(s2[j-2], 1) # last row with matching character
            l = temp
            cost = 0 if s1[i-2] == s2[j-2] else 1
            if not cost:
                temp = j
            arr[i][j] = min(
                arr[i][j-1] + 1, # insertion
                arr[i-1][j] + 1, # deletion                        
                arr[i-1][j-1] + cost, # substitution
                # max: cost of letters between transposed letters
                # 1 addition + 1 deletion = 1 substitution, 1: cost of the transposition itself
                arr[k-1][l-1] + max((i-k-1),(j-l-1)) + 1 # transposition
                )
        charas[s1[i-2]] = i

    # for ar in arr:
    #     print(ar)
        
    return arr[-1][-1]

    
if __name__ == '__main__':
    # print(damerau_levenshtein('kitten', 'sitting'))
    print(damerau_levenshtein('abcdef', 'abcfad'))
    # print(damerau_levenshtein('ca', 'abc'))
    # print(damerau_levenshtein('a cat', 'a abct'))
    # print(damerau_levenshtein('a cat', 'an act'))
    # print(damerau_levenshtein('ifhs', 'fish'))
    # print(damerau_levenshtein('BADC', 'ABCD'))
    # print(damerau_levenshtein('ZX', 'XYZ'))
    # print(damerau_levenshtein('BADC', ''))
    # print(damerau_levenshtein('', 'ABCD'))
    # print(damerau_levenshtein('ABCD', 'ABCD'))
    # print(damerau_levenshtein('', ''))
    # print(damerau_levenshtein('太田佳苗', '田太苗佳'))
