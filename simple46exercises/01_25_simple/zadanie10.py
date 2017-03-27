# Define a function overlapping() that takes two lists
# and returns True if they have at least one member in
# common, False otherwise. You may use your is_member()
# function, or the in operator, but for the sake of the
# exercise, you should (also) write it using two nested
# for-loops.

from simple46exercises.simple.zadanie9 import is_member


def overlapping1(list1, list2):
    for e in list1:
        if e in list2:
            return True
    return False


def overlapping2(list1, list2):
    for e in list1:
        if is_member(e, list2):
            return True
    return False


def overlapping3(list1, list2):
    for a in list1:
        for b in list2:
            if a == b:
                return True
    return False

overlapping = overlapping3


def test(data, result, message):
    print("testing:", data)
    if (overlapping(data[0], data[1]) != result):
        print(message)

if __name__ == '__main__':
    test_all_overlaps = ([1, 2, 3, 4], [1, 2, 3, 4])
    test_first_overlaps = ([1, 2, 3, 4], [1, 5, 6, 7])
    test_middle_overlaps = ([1, 2, 3, 4], [0, 2, 5, 7])
    test_last_overlaps = ([1, 2, 3, 4], [0, 7, 5, 4])
    test_first_list_empty = ([], [1, 2, 3, 4])
    test_last_list_empty = ([1, 2, 3, 4], [])
    test_both_lists_empty = ([], [])
    test_no_overlap = ([1, 3, 5, 7], [2, 4, 6, 8])

    test(test_all_overlaps, True, "lists are the same! result should be True!")
    test(test_first_overlaps, True,
         "first element overlaps! result should be True!")
    test(test_last_overlaps, True,
         "last elements overlaps! result should be True!")
    test(test_middle_overlaps, True,
         "middle element overlaps! result should be True!")
    test(test_first_list_empty, False,
         "first list is empty! result should be False!")
    test(test_last_list_empty, False,
         "last list is empty! result should be False!")
    test(test_both_lists_empty, False,
         "both lists are empty! result should be False!")
    test(test_no_overlap, False,
         "lists do not overlap! result should be False!")
    print("tests completed")
