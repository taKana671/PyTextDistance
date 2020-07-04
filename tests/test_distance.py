import unittest
import cytextdistance


class TestLevenshtein(unittest.TestCase):

    def test_levenshtein(self):
        self.assertEqual(cytextdistance.levenshtein('sitting', 'kitten'), 3)
        self.assertEqual(cytextdistance.levenshtein('sunday', 'saturday'), 3)
        self.assertEqual(cytextdistance.levenshtein('', ''), 0)
        self.assertEqual(cytextdistance.levenshtein('sitting', ''), 7)
        self.assertEqual(cytextdistance.levenshtein('aabcc', 'bccdd'), 4)
        self.assertEqual(cytextdistance.levenshtein('idカード', 'Id番号カード'), 3)
        self.assertEqual(cytextdistance.levenshtein('ひだるま', 'けんだま'), 3)


if __name__ == '__main__':
    unittest.main()