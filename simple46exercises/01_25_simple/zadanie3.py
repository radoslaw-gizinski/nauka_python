# Define a function that computes the length of a given list
# or string. (It is true that Python has the len() function built in,
# but writing it yourself is nevertheless a good exercise


def my_lenght(lista):
    licznik = 0
    for _element in lista:
        licznik = licznik + 1
    return licznik

if __name__ == '__main__':
    lista1 = [1, 2, 3]  # znak = sluzy do przypisania wartosci
    lista_pusta = []
    napis1 = 'witaj swiecie'
    napis_pusty = ''  # '' - napis pusty
    if my_lenght(lista1) == 3:  # == - porownanie wartosci
        print('test 1 OK')
    else:
        print('test 1 ERROR')
    if my_lenght(lista_pusta) == 0:
        print('test 2 OK')
    else:
        print('test 2 ERROR')
    if my_lenght(napis1) == 13:
        print('test 3 OK')
    else:
        print('test 3 ERROR')
    if my_lenght(napis_pusty) == 0:
        print('test 4 OK')
    else:
        print('test 4 ERROR')

    print("dlogosc czgosc tam to ", my_lenght("       print('test 4 ERROR')"))
