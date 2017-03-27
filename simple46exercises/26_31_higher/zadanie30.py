import unittest
'''
Represent a small bilingual lexicon as a Python dictionary in the following
fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott",
"new":"nytt", "year":"�r"} and use it to translate your Christmas cards from
English into Swedish. Use the higher order function map() to write a function
translate() that takes a list of English words and returns a list of Swedish
words.
'''


def translate(text):
    lexicon = {"merry": "god", "christmas": "jul", "and": "och",
               "happy": "gott", "new": "nytt", "year": "år"}
    words = text.split()

    def t(en):
        return lexicon.get(en, en)
    words_se = list(map(t, words))
    return " ".join(words_se)


class Zadanie30Test(unittest.TestCase):
    en_text = "merry christmas and happy new year"
    se_text = "god jul och gott nytt år"

    def test_translate(self):
        self.assertEqual(translate(self.en_text), self.se_text,
                         "wrong transaltion")

    def test_translate_word_not_exist(self):
        self.assertEqual(translate("summer"), "summer",
                         "wrong transaltion")


if __name__ == '__main__':
    unittest.main()
