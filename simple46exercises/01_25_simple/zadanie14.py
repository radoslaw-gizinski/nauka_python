'''
Write a program that maps a list of words into a list of integers representing
the lengths of the correponding words.
'''



def maps_words_into_lenghts(word_list):
    length_list = []
    for w in word_list:
        length_list.append(len(w))
    return length_list

if __name__ == '__main__':
    print(maps_words_into_lenghts(["jeden", "dwa", "trzy"]))

words=["jeden", "dwa", "trzy"]


print([len(w) for w in words])
