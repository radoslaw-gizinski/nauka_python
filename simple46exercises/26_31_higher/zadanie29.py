import unittest
'''
Using the higher order function filter(), define a function filter_long_words()
that takes a list of words and an integer n and returns the list of words that
are longer than n.
'''


def filter_long_words(words, min_length):
    """def longer(w):
        return True if len(w) > min_length else False
    return list(filter(longer, words))"""
    return [w for w in words if len(w) > min_length]


class Zadanie29Test(unittest.TestCase):
    def test_filter_long_words(self):
        words = ["1", "22", "999999999", "7777777", "333", "55555", "4444",
                 "4444", "666666"]
        words_5_longer = ["999999999", "7777777", "666666"]
        self.assertListEqual(filter_long_words(words, 5), words_5_longer,
                             "wrong list of words")

if __name__ == '__main__':
    unittest.main()
