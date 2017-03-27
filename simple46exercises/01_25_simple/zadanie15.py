'''
Write a function find_longest_word() that takes a list of words and returns the
length of the longest one.
'''

from simple46exercises.simple.zadanie14 import maps_words_into_lenghts
from simple46exercises.simple.zadanie13 import max_in_list


def find_longest_word(word_list):
    lenghts = maps_words_into_lenghts(word_list)
    return max_in_list(lenghts)

if __name__ == '__main__':
    test = ["jeden", "dwa", "trzy"]
    print(find_longest_word(test))
