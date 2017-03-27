'''
Represent a small bilingual lexicon as a Python dictionary in the following
fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott",
"new":"nytt", "year":"�r"} and use it to translate your Christmas cards from
English into Swedish. That is, write a function translate() that takes a list
of English words and returns a list of Swedish words.
'''


__eng_2_swe = {"merry": "god", "christmas": "jul", "and": "och",
             "happy": "gott", "new": "nytt", "year": "ar"}


def translate(card_text):
    result = []
    for w in card_text:
        if w.lower() in __eng_2_swe:
            result.append(__eng_2_swe[w.lower()])
        else:
            result.append(w)
    return result

if __name__ == '__main__':
    test = ["Merry", "Christmas", "and", "happy", "new", "year"]
    print(translate(test))
