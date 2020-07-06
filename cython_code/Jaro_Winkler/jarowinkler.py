"""
Jaro distance
The higher the Jaro distance for two strings is, the more similar the strings are.
The score is normalized such that 0 equates to no similarity and 1 is an exact match.
The algorithm is described on:
https://en.wikipedia.org/wiki/Jaro-Winkler_distance
"""
import sys


def jaro_winkler(s1, s2):
    jaro_distance = jaro(s1, s2)
    prefix_len = min(len(prefix(s1, s2)), 4)

    return (jaro_distance + (0.1 * prefix_len * (1.0 - jaro_distance))) * 100.0 / 100.0
    # return round((jaro + (scaling * cl * (1.0 - jaro))) * 100.0) / 100.0


def jaro(s1, s2):
    s1_len, s2_len = len(s1), len(s2)

    if s1_len == 0 and s2_len == 0:
        return 1

    interval = (max(s1_len, s2_len) // 2) - 1

    s1_matches = [0] * s1_len
    s2_matches = [0] * s2_len

    matches, trans = 0, 0

    for i in range(s1_len):
        start = max(0, i - interval)
        end = min(i + interval + 1, s2_len)

        for j in range(start, end):
            if s2_matches[j]:
                continue
            if s1[i] != s2[j]:
                continue
            s1_matches[i] = 1
            s2_matches[j] = 1
            matches += 1
            break

    if matches == 0:
        return 0

    k = 0
    for i in range(s1_len):
        if not s1_matches[i]:
            continue
        while not s2_matches[k]:
            k += 1
        if s1[i] != s2[k]:
            trans += 1
        k += 1

    return ((matches / s1_len) + 
        (matches / s2_len) + 
        ((matches - trans / 2) / matches)) / 3


def prefix(s1, s2):
    if not s1 or not s2:
        return ''

    index = diff_index(s1, s2)
    if index == -1:
        return s1
    elif index == 0:
        return ''
    else:
        return s1[0:index]


def diff_index(s1, s2):
    if s1 == s2:
        return -1

    if not s1 or not s2:
        return 0

    limit = min(len(s1), len(s2))
    for i in range(limit):
        if not s1[i] == s2[i]:
            return i

    return limit


    
    
if __name__ == '__main__':
    args = sys.argv
    if len(args) < 3:
        sys.exit(1)
    print(jaro(args[1], args[2]))
   