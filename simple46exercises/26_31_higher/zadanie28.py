import unittest

'''
Write a function find_longest_word() that takes a list of words and returns the
length of the longest one. Use only higher order functions.
'''


def find_longest_word(words):
    if words == None or len(words) == 0:
        return ""
    the_longest = max([len(w) for w in words])
    return [w for w in words if len(w) == the_longest][0]


class Zadanie28Test(unittest.TestCase):
    def testSimple(self):
        words = ["xxxx", "x", "xxxxx"]
        self.assertEqual(find_longest_word(words), "xxxxx", "wrong word")

    def testEmpty(self):
        words = []
        self.assertEqual(find_longest_word(words), "", "wrong word")

if __name__ == '__main__':
    unittest.main()
