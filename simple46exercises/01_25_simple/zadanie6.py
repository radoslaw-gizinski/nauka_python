# Define a function sum() and a function multiply() that sums and multiplies
# (respectively) all the numbers in a list of numbers. For example,
# sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return
# 24.


def my_sum(numbers):
    result = 0
    for number in numbers:
        result += number
    return result


def multiply(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


if __name__ == '__main__':
    test_data = [1, 2, 3, 4]

    sum_expected_result = 10
    sum_test_result = sum(test_data)
    assert sum_test_result == sum_expected_result, \
        "error. expected %d got %d" \
        % (sum_expected_result, sum_test_result)

    multiply_extepcted_result = 24
    multiply_test_result = multiply(test_data)
    assert multiply_test_result == multiply_extepcted_result, \
        "error, expected %d got %d" \
        % (multiply_extepcted_result, multiply_test_result)
