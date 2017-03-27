'''
Write a procedure char_freq_table() that, when run in a terminal, accepts a
file name from the user, builds a frequency listing of the characters contained
in the file, and prints a sorted and nicely formatted character frequency table
to the screen.
'''

import os
import profile


class CharFreqTable(object):

    def __init__(self, filename):
        self.filename = os.path.abspath(filename)
        self.char_freq = {}
        self._count_chars(self._read_file(filename))

    def _read_file(self, filename):
        try:
            file = open(filename, "rb")
            data = file.read()
            file.close()
            data = [chr(i) for i in data if chr(i).isalpha()]
            return data
        except(FileNotFoundError):
            raise(Exception("nie ma takiego pliku: %s" % self.filename))

    def _count_chars(self, data):
        for c in data:
            if c not in self.char_freq:
                self.char_freq[c] = 1
            self.char_freq[c] += 1

    def __str__(self):
        result = []
        result.append(filename)
        for k in sorted(self.char_freq.keys()):
            result.append("%s = %d" % (k, self.char_freq[k]))
        return "\n".join(result)


if __name__ == '__main__':
    filename = input("podaj plik: ")
    cft = CharFreqTable(filename)
    print(cft)
