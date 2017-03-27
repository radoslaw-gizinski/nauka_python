# Write a function is_member() that takes a value (i.e. a number,
# string, etc) x and a list of values a, and returns True if x is
# a member of a, False otherwise. (Note that this is exactly what
# the in operator does, but for the sake of the exercise you should
# pretend Python did not have this operator.)


def is_member(value, value_list):
    raise NotImplemented


if __name__ == '__main__':
    test1 = (1, [1, 2, 3, 4, 5], True)
    test2 = (1, [0, 2, 3, 4, 5], False)
    assert is_member(test1[0], test1[1]) == test1[2], \
        "error. expected %s" \
        % test1[2]
    assert is_member(test2[0], test2[1]) == test2[2], \
        "error. expected %s" \
        % test2[2]
