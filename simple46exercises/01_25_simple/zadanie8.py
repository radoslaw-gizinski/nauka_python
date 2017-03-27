from simple46exercises.simple.zadanie7 import reverse

# Define a function is_palindrome() that recognizes palindromes
# (i.e. words that look the same written backwards). For example,
# is_palindrome("radar") should return True.


def is_palindrome(text):
    if text.lower() == reverse(text.lower()):
        return True
    else:
        return False


if __name__ == '__main__':
    assert is_palindrome("Radar")
    assert not is_palindrome("test")
