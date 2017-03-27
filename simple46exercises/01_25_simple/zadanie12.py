'''
Define a procedure histogram() that takes a list of integers and prints a
histogram to the screen. For example, histogram([4, 9, 7]) should print the
following:

****
*********
*******
'''

from simple46exercises.simple.zadanie11 import generate_n_chars


def histogram(int_list):
    for i in int_list:
        print(generate_n_chars(i, "*"))
    pass


if __name__ == "__main__":

    histogram([4, 9, 7])
