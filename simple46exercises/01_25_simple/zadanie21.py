import unittest

'''
Write a function char_freq() that takes a string and builds a frequency listing
of the characters contained in it. Represent the frequency listing as a Python
dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab")
'''


def char_freq(text):
    freq = {}
    for c in text:
        if c not in freq:
            freq[c] = 0
        count = freq[c] + 1
        freq[c] = count
    return freq


class Test(unittest.TestCase):

    def test_simple_abc(self):
        test_result = {'a': 1,
                       'b': 1,
                       'c': 1}
        self.assertDictEqual(char_freq("abc"), test_result, "ola!")

    def test_case1(self):
        test_result = {'a': 7, 'b': 14, 'c': 3, 'd': 3}
        self.assertDictEqual(char_freq("abbabcbdbabdbdbabababcbcbab"),
                              test_result, "xx")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
