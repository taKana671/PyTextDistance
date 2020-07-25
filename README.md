# PyTextDistance

PyTextDistance provides implementations to compute distance between two words, using Cython memoryview, Cython array and cpython array.


# Included Algorithms

* Levenshtein Distance
* Damerau-Levenshtein Distance
* Jaro Distance
* Jaro-Winkler Distance
* Hamming Distance


# Requirements

* Python 3.7


# Environment

* Windows10


# Usage

* levenshtein

```bash
>>> from pytextdistance import levenshtein
>>> levenshtein('kitten', 'sitting')
3
```

*  damerau_levenshtein

```bash
>>> from pytextdistance import damerau_levenshtein
>>> damerau_levenshtein('a cat', 'a abct')
2
```

* jaro/jaro_winkler

```bash
>>> from pytextdistance import jaro, jaro_winkler
>>> jaro('dicksonx', 'dixon')
0.7666666666666666
>>> jaro_winkler('dicksonx', 'dixon')
0.8133333333333332
```

* hamming

```bash
>>> from pytextdistance import hamming
>>> hamming('BADC', 'ABCD')
4
```

* compare_distance

```bash
>>> from pytextdistance import compare_distance
>>> compare_distance('kitten', 'sitting')
+-------------+---------------------+-------------------+-------------------+---------+
| Levenshtein | Damerau_Levenshtein | Jaro              | Jaro-Winkler      | Hamming |
+-------------+---------------------+-------------------+-------------------+---------+
| 3           | 3                   | 0.746031746031746 | 0.746031746031746 | *       |
+-------------+---------------------+-------------------+-------------------+---------+

```

* compare_unicode_normalization

```bash
>>> from pytextdistance import compare_unicode_normalization
>>> compare_unicode_normalization('ガ')
+-----------------+-----------------------------+-----------------+-----------------------------+
| NFC             | NFD                         | NFKC            | NFKD                        |
+-----------------+-----------------------------+-----------------+-----------------------------+
| ガ              | ガ                          | ガ              | ガ                          |
+-----------------+-----------------------------+-----------------+-----------------------------+
| b'\xe3\x82\xac' | b'\xe3\x82\xab\xe3\x82\x99' | b'\xe3\x82\xac' | b'\xe3\x82\xab\xe3\x82\x99' |
+-----------------+-----------------------------+-----------------+-----------------------------+

```
