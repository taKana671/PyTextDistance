from collections import OrderedDict

from pytextdistance.cylevenshtein import levenshtein
from pytextdistance.cyjarowinkler import jaro, jaro_winkler
from pytextdistance.cyhamming import hamming
from pytextdistance.tabulator import Tabulator


def compare_distance(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError('Arguments must be str.')
    items = OrderedDict()
    for key, func in zip(('Levenshtein', 'Jaro-Winkler'), (levenshtein, jaro_winkler)):
        items[key] = func(str1, str2)
    items['hamming'] = hamming(str1, str2) if len(str1) == len(str2) else '*'
    tabulator = Tabulator(items)
    print(tabulator.tabulate())






