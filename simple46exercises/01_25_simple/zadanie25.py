import unittest
from simple46exercises.simple.zadanie4 import is_consonant
from simple46exercises.simple.zadanie4 import is_vowel

'''
In English, the present participle is formed by adding the suffix -ing to the
infinite form: go -> going. A simple set of heuristic rules can be given as
follows:

If the verb ends in e, drop the e and add ing (if not exception: be, see, flee,
knee, etc.)
If the verb ends in ie, change ie to y and add ing
For words consisting of consonant-vowel-consonant, double the final letter
before adding ing
By default just add ing
Your task in this exercise is to define a function make_ing_form() which given
a verb in infinitive form returns its present participle form. Test your
function with words such as lie, see, move and hug. However, you must not
expect such simple rules to work for all cases.
'''


def make_ing_form(verb):
    if len(verb) >= 3:
        if (is_consonant(verb[-3:-2])
            and is_vowel(verb[-2:-1])
            and is_consonant(verb[-1:])):
            return verb + verb[-1:] + "ing"
    if verb[-2:] == "ie":
        return verb[:-2] + "ying"
    if verb[-1:] == "e":
        return verb[:-1] + "ing"


class Make_ing_form_Test(unittest.TestCase):

    def test_lie(self):
        self.assertEqual(make_ing_form("lie"), "lying", "wrong form")

    def test_see(self):
        self.assertEqual(make_ing_form("see"), "seing", "wrong form")

    def test_move(self):
        self.assertEqual(make_ing_form("move"), "moving", "wrong form")

    def test_hug(self):
        self.assertEqual(make_ing_form("hug"), "hugging", "wrong form")


if __name__ == '__main__':
    unittest.main()
