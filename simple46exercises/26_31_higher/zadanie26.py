import functools
import unittest

'''
Using the higher order function reduce(), write a function max_in_list() that
takes a list of numbers and returns the largest one. Then ask yourself: why
define and call a new function, when I can just as well call the reduce()
function directly?
'''


def max_in_list(elements):
    if elements == None:
        return None

    def which_one(a, b):
        return a if a > b else b
    return functools.reduce(which_one, elements, None)


class Max_in_list_Test(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(max_in_list([]), None,
                         "no element should be returned for an empty list")

    def text_123(self):
        self.assertEqual(max_in_list([1, 2, 3]), 3, "max is 3")

    def text_42579812(self):
        self.assertEqual(max_in_list(["42579812"]), 9, "max is 9")


if __name__ == '__main__':
    unittest.main()
