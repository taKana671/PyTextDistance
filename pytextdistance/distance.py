from collections import OrderedDict
from itertools import chain
import unicodedata


class Distance:

    def __init__(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2


    
    def unicode_normalization(self):
        pass


    def score(self, calc):
        results = OrderedDict()
        for s1 in self.seq1:
            results[s1] = tuple(calc(s1, s2) for s2 in self.seq2)
        return results
        

    def candidate(self, calc, judge):
        results = OrderedDict()
        for s1 in self.seq1:
            result = tuple(calc(s1, s2) for s2 in self.seq2)
            results[s1] = judge(result)
        return results
                


def unicode_normalization_form(text):
    results = []
    forms = ['NFC', 'NFD', 'NFKC', 'NFKD']
    results.append(forms)
    results.append([unicodedata.normalize(form, text) for form in forms])
    results.append([str(unicodedata.normalize(form, text).encode('utf-8')) for form in forms])
    return results