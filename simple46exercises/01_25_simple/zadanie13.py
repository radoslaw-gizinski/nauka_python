'''
The function max() from exercise 1) and the function max_of_three() from
exercise 2) will only work for two and three numbers, respectively. But suppose
we have a much larger number of numbers, or suppose we cannot tell in advance
how many they are? Write a function max_in_list() that takes a list of numbers
and returns the largest one.ob
'''


def max_in_list(numbers_list):
    _max = numbers_list[0]
    for i in numbers_list:
        if _max < i:
            _max = i
    return _max

if __name__ == '__main__':
    print(max_in_list([-1, 9, 0]))
    print(max_in_list([1, 9, 0]))
    print(max_in_list([11, 9, 0]))
    print(max_in_list([11, 9, 100]))
