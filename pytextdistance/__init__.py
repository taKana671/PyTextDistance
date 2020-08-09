from pytextdistance.cylevenshtein import levenshtein
from pytextdistance.cyjarowinkler import jaro, jaro_winkler
from pytextdistance.cyhamming import hamming
from pytextdistance.cydameraulevenshtein import damerau_levenshtein
from pytextdistance.tabulator import Tabulator
from pytextdistance.distance import Distance, unicode_normalization_form


def compare_distance(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError('Arguments must be str.')
    header = ['Levenshtein', 'Damerau_Levenshtein', 
        'Jaro', 'Jaro-Winkler', 'Hamming']
    results = [func(str1, str2) for func in (
        levenshtein, damerau_levenshtein, jaro, jaro_winkler)]
    results.append(hamming(str1, str2) if len(str1) == len(str2) else '*')
    tabulator = Tabulator([header, results])
    print(tabulator.tabulate())
    

def compare_unicode_normalization(text):
    text = str(text) if not isinstance(text, str) else text
    results = unicode_normalization_form(text)
    tabulator = Tabulator(results)
    print(tabulator.tabulate())


class LevenshteinDistance(Distance):

    def __init__(self):
        super().__init__(levenshtein)

    def _judge(self, dist1, dist2):
        return dist1 < dist2
