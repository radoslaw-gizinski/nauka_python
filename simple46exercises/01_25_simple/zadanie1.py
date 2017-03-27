def mymax(a, b):
    if a > b:
        return a
    else:
        return b


def test_mymax(test_data, test_result, test_id):
    if mymax(test_data[0], test_data[1]) == test_result:
        print("%s is correct" % test_id)
    else:
        print("%s failed!" % test_id)


if __name__ == '__main__':
    lista1 = [1, 5]
    lista2 = [6, 1]
    lista3 = [10, 10]

    test_mymax(lista1, 5, "Test 1")
    test_mymax(lista2, 6, "Test 2")
    test_mymax(lista3, 10, "Test 3")
