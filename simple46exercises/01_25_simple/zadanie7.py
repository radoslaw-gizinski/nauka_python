# Define a function reverse() that computes the reversal of a string.
# For example, reverse("I am testing") should return the string "gnitset ma I".


def reverse(text):
    pass


if __name__ == '__main__':
    test_data = "I am testing"
    expected_result = "gnitset ma I"
    test_result = reverse(test_data)
    assert test_result == expected_result, \
        "error. expected '%s', got '%s'" \
        % (expected_result, test_result)
