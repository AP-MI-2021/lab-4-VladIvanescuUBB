def citire_lista():
    lista = []
    givenString = input("Dati lista, cu elemente separate printr-un spatiu: ")
    numbersAsString = givenString.split(" ")
    for i in numbersAsString:
        lista.append(int(i))
    return lista


def cel_mai_mic(lista):
    """
    functia determina cel mai mic numar dintr-o lista
    :param lista: o lista de numere intregi
    :return: cel mai mic numar din lista
    """
    rezultat = lista[0]
    for i in range(1 , len(lista)):
        if lista[i] < rezultat:
            rezultat = lista[i]
    return rezultat


def test_cel_mai_mic():
    assert cel_mai_mic([1, 2, 3]) == 1
    assert cel_mai_mic([1, -2, 3]) == -2
    assert cel_mai_mic([3, 3, 3]) == 3


def cel_mai_mare(lista):
    """
    functia determina cel mai mare numar dintr-o lista
    :param lista: o lista de numere intregi
    :return: cel mai mare numar din lista
    """
    rezultat = lista[0]
    for i in range(1 , len(lista)):
        if lista[i] > rezultat:
            rezultat = lista[i]
    return rezultat


def test_cel_mai_mare():
    assert cel_mai_mare([1, 2, 3]) == 3
    assert cel_mai_mare([1, 5, 3]) == 5
    assert cel_mai_mare([1, 2, 3, -7]) == 3


def suma_dintre_cel_mai_mare_nr_si_cel_mai_mic_nr(lista):
    """
    functia calculeaza suma dintre cel mai mare număr din listă și cel mai mic număr dintr-o listă
    :param lista: o lista de numere intregi
    :return: suma dintre cel mai mare număr din listă și cel mai mic număr din lista
    """
    return cel_mai_mare(lista) + cel_mai_mic(lista)


def test_suma_dintre_cel_mai_mare_nr_si_cel_mai_mic_nr():
    assert suma_dintre_cel_mai_mare_nr_si_cel_mai_mic_nr([1, 2, 3]) == 4
    assert suma_dintre_cel_mai_mare_nr_si_cel_mai_mic_nr([1, 1, 1]) == 2
    assert suma_dintre_cel_mai_mare_nr_si_cel_mai_mic_nr([1, -2, 3]) == 1



def main():
    test_cel_mai_mic()
    test_cel_mai_mare()
    test_suma_dintre_cel_mai_mare_nr_si_cel_mai_mic_nr()
    print("1. Citirea unei liste de numere întregi. Citirile repetate suprascriu listele precedente.")
    print("2. Afișarea numărului obținut prin concatenarea tuturor numerelor pozitive din listă.")
    print("3. Să se afișeze suma dintre cel mai mare număr din listă și cel mai mic număr din listă.")
    print("0. Iesire")
    while True:
        optiune = int(input("Dati optiune: "))
        if optiune == 1:
            lista = citire_lista()
        elif optiune == 3:
            print(suma_dintre_cel_mai_mare_nr_si_cel_mai_mic_nr(lista))
        elif optiune == 0:
            break
        else:
            print("Optiune gresita! Mai incercati")


main()
