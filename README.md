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

* jaro

```bash
>>> from pytextdistance import jaro
>>> jaro('dicksonx', 'dixon')
```

* jaro_winkler

```bash
>>> from pytextdistance import jaro_winkler
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
>>> compare_unicode_normalization('Ａ')
+-----------------+-----------------+------+------+
| NFC             | NFD             | NFKC | NFKD |
+-----------------+-----------------+------+------+
| Ａ              | Ａ　　　　　　　　| A    | A    |
+-----------------+-----------------+------+------+
| b'\xef\xbc\xa1' | b'\xef\xbc\xa1' | b'A' | b'A' |
+-----------------+-----------------+------+------+
```

