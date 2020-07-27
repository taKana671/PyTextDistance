# from collections import OrderedDict
# from itertools import chain
import unicodedata



class Distance:

    def __init__(self, func):
        self.func = func

    
    def unicode_normalization(self, text, form='NFKC'):
        return unicodedata.normalize(form, text)
        

    def scores(self, seq1, seq2):
        seq2_set = set(seq2)
        for s1 in seq1:
            scores = {s2: self.func(s1, s2) for s2 in seq2_set}
            yield s1, scores
            
     
    
                


def unicode_normalization_form(text):
    results = []
    forms = ['NFC', 'NFD', 'NFKC', 'NFKD']
    results.append(forms)
    results.append([unicodedata.normalize(form, text) for form in forms])
    results.append([str(unicodedata.normalize(form, text).encode('utf-8')) for form in forms])
    return results