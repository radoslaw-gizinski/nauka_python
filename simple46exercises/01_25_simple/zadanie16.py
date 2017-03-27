'''
Write a function filter_long_words() that takes a list of words and an integer
n and returns the list of words that are longer than n.
'''


def filter_long_words(words, min_length):
    result = []
    for w in words:
        if len(w) > min_length:
            result.append(w)
    return result


if __name__ == '__main__':
    test = ["Write", "a", "function", "filter_long_words()", "that", "takes",
            "a", "list", "of", "words", "and", "an", "integer", "n", "and",
            "returns", "the", "list", "of", "words", "that", "are", "longer",
            "than", "n."]

    print(filter_long_words(test, 10))
    print(filter_long_words(test, 7))
    print(filter_long_words(test, 3))
