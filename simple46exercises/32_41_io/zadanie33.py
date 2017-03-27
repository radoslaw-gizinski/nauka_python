import unittest
import re

'''
According to Wikipedia, a semordnilap is a word or phrase that spells a
different word or phrase backwards. ("Semordnilap" is itself "palindromes"
spelled backwards.) Write a semordnilap recogniser that accepts a file name
(pointing to a list of words) from the user and finds and prints all pairs of
words that are semordnilaps to the screen. For example, if "stressed" and
"desserts" is part of the word list, the the output should include the pair
"stressed desserts". Note, by the way, that each pair by itself forms a
palindrome!
'''


def load_words(filename):
    """
    Load words from file and strips them from all non alpha characters.
    1 letter words are not considered as a valid word
    """
    f = open(filename)
    known_words = set()
    for line in f:
        known_words.update(line.split())
    f.close()
    clean_words = set(clean_word(w) for w in known_words
                      if len(clean_word(w)) > 1)
    return clean_words


def clean_word(word):
    """
    cleans words from non alpha characters
    returns empty string if no valid word was passed
    """
    try:
        match = re.search(r"(?P<clean_word>\w+)", word)
        return match.group('clean_word')
    except (AttributeError):
        return ""


def find_semordnilaps(filename):
    """
    finds pairs of words in a file which are palindromes for each other
    like desserts is a palindrome for stressesd
    """
    words = load_words(filename)
    semordnilaps = set(w for w in words if w[::-1] in words)
    pairs = set()
    already_added = set()
    for word in semordnilaps:
        if word not in already_added:
            pairs.add((word, word[::-1]))
            already_added.add(word)
            already_added.add(word[::-1])
    return pairs


class Zadanie32Test(unittest.TestCase):
    def test_clean_word(self):
        self.assertEqual(clean_word("('\"!-:test!!@#$"), "test",
                         "word not clean")

    def test_clean_word_non_word(self):
        self.assertEqual(clean_word("'"''), "", "should be empty string")

    def test_load_words(self):
        words = set("stressed desserts Note by the way that each pair"
                    " by itself forms palindrome".split())
        self.assertSetEqual(load_words("load_words_test.txt"), words,
                            "wrong words list")

    def test_find_semodnilaps(self):
        result = {('semordnilap', 'palindromes'), ('stressed', 'desserts')}
        self.assertSetEqual(find_semordnilaps("zadanie33.py"), result,
                            "wrong result")


if __name__ == '__main__':
    unittest.main()
