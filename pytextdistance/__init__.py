from pytextdistance.cylevenshtein import levenshtein, normalized_levenshtein
from pytextdistance.cyjarowinkler import jaro, jaro_winkler
from pytextdistance.cyhamming import hamming
from pytextdistance.cydameraulevenshtein import damerau_levenshtein
from pytextdistance.tabulator import Tabulator
from pytextdistance.distance import *
from pytextdistance.outputfile import ExcelHandler, CsvHandler, TextFileHandler


def compare_distances(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError('Arguments must be str.')
    header = ['Levenshtein', 'Damerau_Levenshtein', 'Normalized_Levenshtein'
        'Jaro', 'Jaro-Winkler', 'Hamming']
    results = [func(str1, str2) for func in (
        levenshtein, damerau_levenshtein, normalized_levenshtein, jaro, jaro_winkler)]
    results.append(hamming(str1, str2) if len(str1) == len(str2) else '*')
    tabulator = Tabulator([header, results])
    print(tabulator.tabulate())
    

def compare_unicode_normalization(text):
    text = str(text) if not isinstance(text, str) else text
    results = unicode_normalization_form(text)
    tabulator = Tabulator(results)
    print(tabulator.tabulate())





