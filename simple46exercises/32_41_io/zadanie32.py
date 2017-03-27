import unittest
'''
Write a version of a palindrome recogniser that accepts a file name from the
user, reads each line, and prints the line to the screen if it is a palindrome.
'''
from simple46exercises.simple.zadanie8 import is_palindrome


def load_palindromes():
    palindromes = []
    f = open("zadanie32.txt")
    for line in f:
        if is_palindrome(line.strip()):
            palindromes.append(line.strip())
    f.close()
    return palindromes


class ZadanieTest(unittest.TestCase):
    def test(self):
        known_palindromes = ["radar",
                              "ala",
                              "alla",
                              "abcba",
                               "abba"]
        self.assertListEqual(load_palindromes(), known_palindromes,
                             "wring list")


if __name__ == '__main__':
    unittest.main()
