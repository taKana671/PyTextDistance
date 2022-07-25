import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir('..')

from pytextdistance import levenshtein
from pytextdistance import normalized_levenshtein
from pytextdistance import jaro
from pytextdistance import jaro_winkler
from pytextdistance import hamming
from pytextdistance import damerau_levenshtein
from pytextdistance_go import levenshtein as levenshtein_go
from pytextdistance_go import normalized_levenshtein as normalized_levenshtein_go
from pytextdistance_go import jaro as jaro_go
from pytextdistance_go import jaro_winkler as jaro_winkler_go
from pytextdistance_go import hamming as hamming_go
from pytextdistance_go import damerau_levenshtein as damerau_levenshtein_go


class TestLevenshtein(unittest.TestCase):

    def setUp(self):
        self.cases_success = [
            ('sitting', 'kitten', 3),
            ('sunday', 'saturday', 3),
            ('', '', 0),
            ('sitting', '', 7),
            ('aabcc', 'bccdd', 4),
            ('idカード', 'Id番号カード', 3),
            ('ひだるま', 'けんだま', 3)
        ]
        self.cases_failed = [
            ('abc', 1),
            (1, 'abc'),
            (5, 1)
        ]

    def test_levenshtein(self):
        for str1, str2, expected in self.cases_success:
            with self.subTest(str1=str1, str2=str2):
                self.assertEqual(levenshtein(str1, str2), expected)

    def test_levenshtein_go(self):
        for str1, str2, expected in self.cases_success:
            with self.subTest(str1=str1, str2=str2):
                self.assertEqual(levenshtein_go(str1, str2), expected)

    def test_invalid_args(self):
        for str1, str2 in self.cases_failed:
            with self.subTest(str1=str1, str2=str2):
                with self.assertRaises(TypeError):
                    levenshtein(str1, str2)

    def test_invalid_args_go(self):
        for str1, str2 in self.cases_failed:
            with self.subTest(str1=str1, str2=str2):
                with self.assertRaises(AttributeError):
                    levenshtein_go(str1, str2)


class TestJaro(unittest.TestCase):

    def setUp(self):
        self.cases_success = [
            ('abc', 'bac', 0.8888888888888888),
            ('dicksonx', 'dixon', 0.7666666666666666),
            ('dixon', 'dicksonx', 0.7666666666666666),
            ('Brian', 'Jesus', 0.0),
            ('Thorkel', 'Thorgier', 0.7797619047619048),
            ('Dinsdale', 'D', 0.7083333333333334),
            ('Carol', 'elephant', 0.44166666666666665),
            ('', '', 1.0),
            ('Dinsdale', '', 0.0),
            ('', 'elephant', 0.0),
            ('idカード', 'Id番号', 0.48333333333333334),
            ('ひだるま', 'けんだま', 0.6666666666666666)
        ]
        self.cases_failed = [
            ('abc', 1),
            (1, 'abc'),
            (5, 1)    
        ]

    def test_jaro(self):
        for str1, str2, expected in self.cases_success:
            with self.subTest(str1=str1, str2=str2):
                self.assertEqual(jaro(str1, str2), expected)

    def test_jaro_go(self):
        for str1, str2, expected in self.cases_success:
            with self.subTest(str1=str1, str2=str2):
                self.assertEqual(jaro_go(str1, str2), expected)

    def test_invalid_args(self):
        for str1, str2 in self.cases_failed:
            with self.subTest(str1=str1, str2=str2):
                with self.assertRaises(TypeError):
                    jaro(str1, str2)

    def test_invalid_args_go(self):
        for str1, str2 in self.cases_failed:
            with self.subTest(str1=str1, str2=str2):
                with self.assertRaises(AttributeError):
                    jaro_go(str1, str2)


class TestJaroWinkler(unittest.TestCase):

    def setUp(self):
        self.cases_success = [
            ('abc', 'bac', 0.8888888888888888),
            ('dicksonx', 'dixon', 0.8133333333333332),
            ('dixon', 'dicksonx', 0.8133333333333332),
            ('Brian', 'Jesus', 0.0),
            ('Thorkel', 'Thorgier', 0.8678571428571429),
            ('Dinsdale', 'D', 0.7375),
            ('Carol', 'elephant', 0.44166666666666665),
            ('', '', 1.0),
            ('Dinsdale', '', 0.0),
            ('', 'elephant', 0.0),
            ('idカード', 'Id番号', 0.48333333333333334),
            ('ひだるま', 'けんだま', 0.6666666666666666),
        ]
        self.cases_failed = [
            ('abc', 1),
            (1, 'abc'),
            (5, 1)    
        ]

    def test_jaro_winkler(self):
        for str1, str2, expected in self.cases_success:
            with self.subTest(str1=str1, str2=str2):
                self.assertEqual(jaro_winkler(str1, str2), expected)

    def test_jaro_winkler_go(self):
        for str1, str2, expected in self.cases_success:
            with self.subTest(str1=str1, str2=str2):
                self.assertEqual(jaro_winkler_go(str1, str2), expected)

    def test_invalid_args(self):
        for str1, str2 in self.cases_failed:
            with self.subTest(str1=str1, str2=str2):
                with self.assertRaises(TypeError):
                    jaro_winkler(str1, str2)

    def test_invalid_args_go(self):
        for str1, str2 in self.cases_failed:
            with self.subTest(str1=str1, str2=str2):
                with self.assertRaises(AttributeError):
                    jaro_winkler_go(str1, str2)


class TestHamming(unittest.TestCase):

    def setUp(self):
        self.cases_success = [
            ('karolin', 'kathrin', 3),
            ('karolin', 'kerstin', 3),
            ('kathrin', 'kerstin', 4),
            ('1011101', '1001001', 2),
            ('2173896', '2233796', 3),
            ('Brian', 'Jesus', 5),
            ('Brian', 'Brian', 0)
        ]

    def test_hamming(self):
        for str1, str2, expected in self.cases_success:
            with self.subTest(str1=str1, str2=str2):
                self.assertEqual(hamming(str1, str2), expected)

    def test_hamming_go(self):
        for str1, str2, expected in self.cases_success:
            with self.subTest(str1=str1, str2=str2):
                self.assertEqual(hamming_go(str1, str2), expected)

    def test_invalid_args(self):
        cases = [
            ('abc', 1, TypeError),
            ('abc', 'abcdf', ValueError)
        ]
        for str1, str2, exception in cases:
            with self.subTest(str1=str1, str2=str2):
                with self.assertRaises(exception):
                    hamming(str1, str2)

    def test_invalid_args_go(self):
        cases = [
            ('abc', 1, AttributeError),
            ('abc', 'abcdf', ValueError)
        ]
        for str1, str2, exception in cases:
            with self.subTest(str1=str1, str2=str2):
                with self.assertRaises(exception):
                    hamming_go(str1, str2)


class TestDamerauLevenshtein(unittest.TestCase):

    def setUp(self):
        self.cases_success = [
            ('abcdef', 'abcfad', 2),
            ('ca', 'abc', 2),
            ('a cat', 'a abct', 2),
            ('a cat', 'an act', 2),
            ('ifhs', 'fish', 2),
            ('BADC', 'ABCD', 2),
            ('ZX', 'XYZ', 2),
            ('BADC', '', 4),
            ('', 'ABCD', 4),
            ('ABCD', 'ABCD', 0),
            ('', '', 0),
        ]

    def test_damerau_levenshtein(self):
        for str1, str2, expected in self.cases_success:
            with self.subTest(str1=str1, str2=str2):
                self.assertEqual(damerau_levenshtein(str1, str2), expected)

    def test_damerau_levenshtein_go(self):
        for str1, str2, expected in self.cases_success:
            with self.subTest(str1=str1, str2=str2):
                self.assertEqual(damerau_levenshtein_go(str1, str2), expected)

    def test_invalid_args(self):
        self.assertRaises(TypeError, damerau_levenshtein, 'abc', 1)

    def test_invalid_args_go(self):
        self.assertRaises(AttributeError, damerau_levenshtein_go, 'abc', 1)
        

class TestNormalizedLevenshtein(unittest.TestCase):

    def setUp(self):
        self.cases_success = [
            ('アイス', 'ミント', 1.0),
            ('チョコレート', 'チョコレートアイス', 0.3333333333333333),
            ('dixon', 'dickson', 0.42857142857142855),
            ('sunday', 'saturday', 0.375),
        ]
        self.cases_failed = [
            ('abc', 1),
            (1, 'abc'),
            (5, 1)    
        ]

    def test_normalized_levenshtein(self):
        for str1, str2, expected in self.cases_success:
            with self.subTest(str1=str1, str2=str2):
                self.assertEqual(normalized_levenshtein(str1, str2), expected)

    def test_normalized_levenshtein_go(self):
        for str1, str2, expected in self.cases_success:
            with self.subTest(str1=str1, str2=str2):
                self.assertEqual(normalized_levenshtein_go(str1, str2), expected)

    def test_invalid_args(self):
        for str1, str2 in self.cases_failed:
            with self.subTest(str1=str1, str2=str2):
                with self.assertRaises(TypeError):
                    normalized_levenshtein(str1, str2)

    def test_invalid_args_go(self):
        for str1, str2 in self.cases_failed:
            with self.subTest(str1=str1, str2=str2):
                with self.assertRaises(AttributeError):
                    normalized_levenshtein_go(str1, str2)
      

if __name__ == '__main__':
    unittest.main()
