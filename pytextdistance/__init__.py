from pytextdistance.cylevenshtein import levenshtein
from pytextdistance.cyjarowinkler import jaro, jaro_winkler
from pytextdistance.cyhamming import hamming
from pytextdistance.tabulator import Tabulator
from pytextdistance.distance import *


def compare_distance(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError('Arguments must be str.')
    header = ['Levenshtein', 'Jaro-Winkler', 'Hamming']
    results = [func(str1, str2) for func in (levenshtein, jaro_winkler)]
    results.append(hamming(str1, str2) if len(str1) == len(str2) else '*')
    tabulator = Tabulator([header, results])
    print(tabulator.tabulate())
    


def compare_unicode_normalization(text):
    text = str(text) if not isinstance(text, str) else text
    results = unicode_normalization_form(text)
    tabulator = Tabulator(results)
    print(tabulator.tabulate())


