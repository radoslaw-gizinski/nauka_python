import unittest

'''
The third person singular verb form in English is distinguished by the suffix
-s, which is added to the stem of the infinitive form: run -> runs. A simple
set of rules can be given as follows:

If the verb ends in y, remove it and add ies
If the verb ends in o, ch, s, sh, x or z, add es
By default just add s
Your task in this exercise is to define a function make_3sg_form() which given
a verb in infinitive form returns its third person singular form. Test your
function with words like try, brush, run and fix. Note however that the rules
must be regarded as heuristic, in the sense that you must not expect them to
work for all cases. Tip: Check out the string method endswith().
'''


def make_3sg_form(text):
    if text.endswith("y"):
        return text[:-1] + "ies"
    es_endings = ["o", "ch", "s", "sh", "x", "z"]
    for e in es_endings:
        if text.endswith(e):
            return text + "es"
    return text + "s"


class Make_3sg_form_Test(unittest.TestCase):

    def test_try(self):
        self.assertEqual(make_3sg_form("try"), "tries", "wrong form")

    def test_brush(self):
        self.assertEqual(make_3sg_form("brush"), "brushes", "wrong form")

    def test_run(self):
        self.assertEqual(make_3sg_form("run"), "runs", "wrong form")

    def text_fix(self):
        self.assertEqual(make_3sg_form("fix"), "fixes", "wrong form")

if __name__ == '__main__':
    unittest.main()
