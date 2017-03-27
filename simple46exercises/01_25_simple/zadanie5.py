from simple46exercises.simple.zadanie4 import is_vowel

# Write a function translate() that will translate a text into "rovarsprlket"
# (Swedish for "robber's language"). That is, double every consonant and place
# an occurrence of "o" in between. For example, translate("this is fun") should
# return the string "tothohisos isos fofunon".

# TODO fix source according to PEP8
# XXX test to do
# FIX to jest fix
# FIXME a to jest fixme


def translate3(text):
    result = ""
    for c in text:
        if not is_vowel(c) and c.isalpha():
            result += ''.join([c, 'o', c])
        else:
            result += c
    return result


def translate2(text):
    result = ""
    for c in text:
        if is_vowel(c) or c == ' ':
            result += c
        else:
            result += ''.join([c, 'o', c])
    return result


def translate1(text):
    result = ""
    for c in text:
        if is_vowel(c):
            result += c
        else:
            result += ''.join([c, 'o', c])
    return result

translate = translate1

if __name__ == "__main__":
    test_result = translate("this is fun")
    expected = "tothohisos isos fofunon"
    assert test_result == expected, \
        "wrong translation. expected %s, got %s" \
        % (expected, test_result)
