import unittest
from cytextdistance import levenshtein, jaro, jaro_winkler


class TestLevenshtein(unittest.TestCase):

    def test_levenshtein(self):
        self.assertEqual(levenshtein('sitting', 'kitten'), 3)
        self.assertEqual(levenshtein('sunday', 'saturday'), 3)
        self.assertEqual(levenshtein('', ''), 0)
        self.assertEqual(levenshtein('sitting', ''), 7)
        self.assertEqual(levenshtein('aabcc', 'bccdd'), 4)
        self.assertEqual(levenshtein('idカード', 'Id番号カード'), 3)
        self.assertEqual(levenshtein('ひだるま', 'けんだま'), 3)


    def test_invalid_args(self):
        self.assertRaises(TypeError, levenshtein, 'abc', 1)
        self.assertRaises(TypeError, levenshtein, 1, 'abc')
        self.assertRaises(TypeError, levenshtein, 5, 1)


class TestJaro(unittest.TestCase):

    def test_jaro(self):
        self.assertEqual(jaro('abc', 'bac'), 0.8888888888888888)
        self.assertEqual(jaro('dicksonx', 'dixon'), 0.7666666666666666)
        self.assertEqual(jaro('dixon', 'dicksonx'), 0.7666666666666666)
        self.assertEqual(jaro('Brian', 'Jesus'), 0.0)
        self.assertEqual(jaro('Thorkel', 'Thorgier'), 0.7797619047619048)
        self.assertEqual(jaro('Dinsdale', 'D'), 0.7083333333333334)
        self.assertEqual(jaro('Carol','elephant'), 0.44166666666666665)
        self.assertEqual(jaro('', ''), 1.0)
        self.assertEqual(jaro('Dinsdale', ''), 0.0)
        self.assertEqual(jaro('','elephant'), 0.0)
        self.assertEqual(jaro('idカード', 'Id番号'), 0.48333333333333334)
        self.assertEqual(jaro('ひだるま', 'けんだま'), 0.6666666666666666)


    def test_invalid_args(self):
        self.assertRaises(TypeError, jaro, 'abc', 1)
        self.assertRaises(TypeError, jaro, 1, 'abc')
        self.assertRaises(TypeError, jaro, 5, 1)


class TestJaroWinkler(unittest.TestCase):

    def test_jaro(self):
        self.assertEqual(jaro_winkler('abc', 'bac'), 0.8888888888888888)
        self.assertEqual(jaro_winkler('dicksonx', 'dixon'), 0.8133333333333332)
        self.assertEqual(jaro_winkler('dixon', 'dicksonx'), 0.8133333333333332)
        self.assertEqual(jaro_winkler('Brian', 'Jesus'), 0.0)
        self.assertEqual(jaro_winkler('Thorkel', 'Thorgier'), 0.8678571428571429)
        self.assertEqual(jaro_winkler('Dinsdale', 'D'), 0.7375)
        self.assertEqual(jaro_winkler('Carol','elephant'), 0.44166666666666665)
        self.assertEqual(jaro_winkler('', ''), 1.0)
        self.assertEqual(jaro_winkler('Dinsdale', ''), 0.0)
        self.assertEqual(jaro_winkler('','elephant'), 0.0)
        self.assertEqual(jaro('idカード', 'Id番号'), 0.48333333333333334)
        self.assertEqual(jaro('ひだるま', 'けんだま'), 0.6666666666666666)
        

    def test_invalid_args(self):
        self.assertRaises(TypeError, jaro, 'abc', 1)
        self.assertRaises(TypeError, jaro, 1, 'abc')
        self.assertRaises(TypeError, jaro, 5, 1)


if __name__ == '__main__':
    unittest.main()