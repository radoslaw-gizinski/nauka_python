import unittest

'''
Write a program that maps a list of words into a list of integers representing
the lengths of the correponding words. Write it in three different ways: 1)
using a for-loop, 2) using the higher order function map(), and 3) using list
comprehensions.
'''


def words_to_ints_for(words):
    l = []
    for w in words:
        l.append(len(w))
    return l


def words_to_ints_map(words):
    return list(map(len, words))


def words_to_ints_com(words):
    return [len(w) for w in words]


class Zadanie27Test(unittest.TestCase):
    def test_short_for(self):
        words = ["x", "xx", "xxx"]
        ints = [1, 2, 3]
        self.assertListEqual(words_to_ints_for(words), ints, "wrong result")

    def test_short_map(self):
        words = ["x", "xx", "xxx"]
        ints = [1, 2, 3]
        self.assertListEqual(words_to_ints_map(words), ints, "wrong result")

    def test_short_com(self):
        words = ["x", "xx", "xxx"]
        ints = [1, 2, 3]
        self.assertListEqual(words_to_ints_com(words), ints, "wrong result")


if __name__ == '__main__':
    unittest.main()
