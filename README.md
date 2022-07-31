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

### pytextdistance

* Cython implementations to compute distance between two words.

```bash
>>> from pytextdistance import levenshtein
>>> levenshtein('kitten', 'sitting')
3

>>> from pytextdistance import damerau_levenshtein
>>> damerau_levenshtein('a cat', 'a abct')
2

>>> from pytextdistance import normalized_levenshtein
>>> normalized_levenshtein('sunday', 'saturday')
0.375

>>> from pytextdistance import jaro
>>> jaro('dicksonx', 'dixon')
0.7666666666666666

>>> from pytextdistance import jaro_winkler
>>> jaro_winkler('dicksonx', 'dixon')
0.8133333333333332

>>> from pytextdistance import hamming
>>> hamming('BADC', 'ABCD')
4
```

### pytextdistance_go

* A library for Python, made with Go lang.

```bash
>>> from pytextdistance_go import levenshtein as levenshtein_go
>>> levenshtein_go('kitten', 'sitting')
3

>>> from pytextdistance_go import damerau_levenshtein as damerau_levenshtein_go
>>> damerau_levenshtein_go('a cat', 'a abct')
2

>>> from pytextdistance_go import normalized_levenshtein as normalized_levenshtein_go 
>>> normalized_levenshtein_go('sunday', 'saturday')
0.375

>>> from pytextdistance_go import jaro as jaro_go
>>> jaro_go('dicksonx', 'dixon')
0.7666666666666666

>>> from pytextdistance_go import jaro_winkler as jaro_winkler_go
>>> jaro_winkler('dicksonx', 'dixon')
0.8133333333333332

>>> from pytextdistance_go import hamming as hamming_go
>>> hamming_go('BADC', 'ABCD')
4
```
