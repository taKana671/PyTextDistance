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

* damerau_levenshtein

```bash
>>> from pytextdistance import damerau_levenshtein
>>> damerau_levenshtein('a cat', 'a abct')
2
```

* normalized_levenshtein

```bash
>>> from pytextdistance import normalized_levenshtein
>>> normalized_levenshtein('sunday', 'saturday')
0.375
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
>>> compare_distance('dicksonx', 'dixon')
+-------------+---------------------+--------------------+--------------------+---------+
| Levenshtein | Damerau_Levenshtein | Jaro               | Jaro-Winkler       | Hamming |
+-------------+---------------------+--------------------+--------------------+---------+
| 4           | 4                   | 0.7666666666666666 | 0.8133333333333332 | *       |
+-------------+---------------------+--------------------+--------------------+---------+

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

* *class*  pytextdistance.LevenshteinDistance
* *class*  pytextdistance.DamerauLevenshteinDistance
* *class*  pytextdistance.NormalizedLevenshteinDistance
* *class*  pytextdistance.JaroWinklerDistance

  ## methods            
  * unicode_normalization(text, form)
    Return normalized text.
    ### Parameters:
    * text - string
    * form - 'NFKC'(default),'NFC', 'NFD', 'NFKD'

  * scores(seq1, seq2)
  * multiprocess_scores(seq1, seq2)
  
  ```bash
  >>> from pytextdistance import LevenshteinDistance
  >>> seq1 = ['James', 'Harold', 'Jaxon']
  >>> seq2 = ['Carol', 'Jane', 'Joson', 'Jack', 'Harry']
  >>> leven = LevenshteinDistance()
  >>> for scores in leven.scores(seq1, seq2):
  ...    print(scores)

  {'text': 'James', 'Carol': 4, 'Jane': 2, 'Joson': 4, 'Jack': 3, 'Harry': 4}
  {'text': 'Harold', 'Carol': 2, 'Jane': 5, 'Joson': 5, 'Jack': 5, 'Harry': 3}
  {'text': 'Jaxon', 'Carol': 3, 'Jane': 3, 'Joson': 2, 'Jack': 3, 'Harry': 4}
  ```  

  * candidate(seq1, seq2) 
  * multiprocess_candidate(seq1, seq2)

  ```bash
  >>> from pytextdistance import LevenshteinDistance
  >>> seq1 = ['James', 'Harold', 'Jaxon']
  >>> seq2 = ['Carol', 'Jane', 'Joson', 'Jack', 'Harry']
  >>> leven = LevenshteinDistance()
  >>> for candidate in leven.candidate(seq1, seq2):
  ...     print(candidate)

  {'text': 'James', 'candidate': 'Jane'}
  {'text': 'Harold', 'candidate': 'Carol'}
  {'text': 'Jaxon', 'candidate': 'Joson'}

  ```

  * scores_to_file(records, dir, file_type='xlsx')
  * candidate_to_file(records, dir, file_type='xlsx')
    Ouput results to a file.
    ## Parameters:
    * dir - folder path
    * file_type - 'xlsx'(default), 'txt', 'csv'

  ```bash
  >>> from pytextdistance import LevenshteinDistance
  >>> seq1 = ['James', 'Harold', 'Jaxon']
  >>> seq2 = ['Carol', 'Jane', 'Joson', 'Jack', 'Harry']
  >>> leven = LevenshteinDistance()
  >>> leven.scores_to_file(leven.scores(seq1, seq2), path, 'csv')
  >>> leven.scores_to_file(leven.multiprocess_scores(seq1, seq2), path, 'csv')
  ```
   



