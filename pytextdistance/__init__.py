from collections import OrderedDict

from cytextdistance.cylevenshtein import levenshtein
from cytextdistance.cyjarowinkler import jaro, jaro_winkler
from cytextdistance.tabulator import Tabulator


def compare_distance(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError('Arguments must be str.')
    items = OrderedDict()
    items['string1'], items['string2']= str1, str2  
    for key, func in zip(('Levenshtein', 'Jaro-Winkler'), (levenshtein, jaro_winkler)):
        items[key] = func(str1, str2)
    tabulator = Tabulator(items)
    print(tabulator.tabulate())






