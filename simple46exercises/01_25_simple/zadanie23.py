import unittest

'''
Define a simple "spelling correction" function correct() that takes a string
and sees to it that 1) two or more occurrences of the space character is
compressed into one, and 2) inserts an extra space after a period if the period
is directly followed by a letter.
E.g. correct("This   is  very funny  and    cool.Indeed!") should return
"This is very funny and cool. Indeed!" Tip: Use regular
expressions!
'''


def correct(text):
    chars = []
    last_char = ''
    for c in text:
        if c == " " and last_char == " ":
            pass
        elif c.isalnum() and last_char == ".":
            chars.append(" ")
            chars.append(c)
        else:
            chars.append(c)
        last_char = c
    return ''.join(chars)


class CorrectTest(unittest.TestCase):

    def test_correct(self):
        test = "This   is  very funny  and    cool.Indeed!"
        expected = "This is very funny and cool. Indeed!"
        self.assertEqual(correct(test), expected, "not correct")

if __name__ == '__main__':
    unittest.main()
