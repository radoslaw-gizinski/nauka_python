def is_vowel(c):
    '''
    To jest dokumentacja funkcji
    Zwraca True jezeli c jest samogloska (a, e, i, o, u, y). W przeciwnym
    wypadku zwraca False
    '''
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    if c.lower() in vowels:
        return True
    else:
        return False


def is_consonant(c):
    return not is_vowel(c) and c.isalpha()


if __name__ == '__main__':
    assert is_vowel('a'), "Blad! a jest samogloska!"
    assert is_vowel('A'), "Blad! A jest samogloska!"
    assert not is_vowel('b'), "Blad! b jest spolgloska!"
    assert not is_vowel(' '), "Blad! spacja nie jest samogloska!"
