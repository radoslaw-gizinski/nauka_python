'''
Write a version of a palindrome recognizer that also accepts phrase palindromes
such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on
no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan,
oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
t"Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that
punctuation, capitalization, and spacing are usually ignored.
'''

from simple46exercises.simple.zadanie8 import is_palindrome


def phrase_palindrome(text):
    stripped_text = []
    for c in text:
        if c.isalpha():
            stripped_text.append(c.lower())
    stripped_text = ''.join(stripped_text)
    return is_palindrome(stripped_text)


if __name__ == '__main__':
    test = "Go hang a salami I'm a lasagna hog."
    print("testing '%s': %s" % \
          (test, phrase_palindrome("Go hang a salami I'm a lasagna hog.")))
