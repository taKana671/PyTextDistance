import ctypes


class GoString(ctypes.Structure):

    _fields_ = [('p', ctypes.c_char_p), ('n', ctypes.c_longlong)]


lib = ctypes.cdll.LoadLibrary('./pytextdistance_go/gotextdistance.so')

go_hamming = lib.Hamming
go_hamming.argtypes = (GoString, GoString)

go_levenshtein = lib.Levenshtein
go_levenshtein.argtypes = (GoString, GoString)

go_damerau = lib.DamerauLevenshtein
go_damerau.argtypes = (GoString, GoString)

go_normalized = lib.NormalizedLevenshtein
go_normalized.argtypes = (GoString, GoString)
go_normalized.restype = ctypes.c_double

go_jaro = lib.Jaro
go_jaro.argtypes = (GoString, GoString)
go_jaro.restype = ctypes.c_double

go_winkler = lib.JaroWinkler
go_winkler.argtypes = (GoString, GoString)
go_winkler.restype = ctypes.c_double


def cast(s1, s2):
    s1 = s1.encode('utf-8')
    s2 = s2.encode('utf-8')

    return GoString(s1, len(s1)), GoString(s2, len(s2))


def hamming(s1, s2):
    s1, s2 = cast(s1, s2)
    distance = go_hamming(s1, s2)
    if distance == -1:
        raise ValueError('expected two strings of the same length')
    return distance


def levenshtein(s1, s2):
    s1, s2 = cast(s1, s2)
    return go_levenshtein(s1, s2)


def damerau_levenshtein(s1, s2):
    s1, s2 = cast(s1, s2)
    return go_damerau(s1, s2)


def normalized_levenshtein(s1, s2):
    s1, s2 = cast(s1, s2)
    return go_normalized(s1, s2)


def jaro(s1, s2):
    s1, s2 = cast(s1, s2)
    return go_jaro(s1, s2)


def jaro_winkler(s1, s2):
    s1, s2 = cast(s1, s2)
    return go_winkler(s1, s2)