def is_vowel(c):
    pass

def is_consonant(c):
    pass


if __name__ == '__main__':
    assert is_vowel('a'), "Blad! a jest samogloska!"
    assert is_vowel('A'), "Blad! A jest samogloska!"
    assert not is_vowel('b'), "Blad! b jest spolgloska!"
    assert not is_vowel(' '), "Blad! spacja nie jest samogloska!"
