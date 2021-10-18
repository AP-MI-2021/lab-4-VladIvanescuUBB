def afisare_meniu():
    print("1. Citirea unei liste de numere întregi. Citirile repetate suprascriu listele precedente.")
    print("2. Afișarea numărului obținut prin concatenarea tuturor numerelor pozitive din listă.")
    print("3. Să se afișeze suma dintre cel mai mare număr din listă și cel mai mic număr din listă.")
    print("4. Afișarea tuturor numerelor care au suma cifrelor mai mare sau egală decat"
          "un număr n citit de la tastatură.")
    print("5. Afișarea listei obținute din lista inițială în care numerele pătrat perfect sunt înlocuite"
          "cu radicalul acestora. În cazul numerelor care nu sunt pătrat perfect, acestea sunt înlocuite"
          "cu o listă cu numerele pătrat perfect mai mici decât numărul inițial."
          "Modificările se aplică doar pe numerele pozitive.")
    print("0. Iesire")


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
    for i in range(1, len(lista)):
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
    for i in range(1, len(lista)):
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


def suma_cifrelor(numar):
    """
    functia calculeaza suma cifrelor unui numar
    :param numar: un numar intreg
    :return: suma cifrelor lui numar
    """
    if numar < 0:
        numar = numar * -1
    rezultat = 0
    while numar > 0:
        rezultat = rezultat + numar % 10
        numar = numar // 10
    return rezultat


def test_suma_cifrelor():
    assert suma_cifrelor(12) == 3
    assert suma_cifrelor(5) == 5
    assert suma_cifrelor(-35) == 8


def afisare_nr_cu_sum_cif(lista, n):
    """
    functia afiseaza toate numerele dintr-o lista care au suma cifrelor mai mare sau egală decat un număr
    :param lista: o lista de numere intregi
    :param n: un numar intreg
    :return: toate numerele din lista care au suma cifrelor mai mare sau egală decat n
    """
    rezultat = []
    for i in lista:
        if suma_cifrelor(i) >= n:
            rezultat.append(i)
    return rezultat


def test_afisare_nr_cu_sum_cif():
    assert afisare_nr_cu_sum_cif([12, 67, 42], 10) == [67]
    assert afisare_nr_cu_sum_cif([12, 67, 42, 89], 10) == [67, 89]
    assert afisare_nr_cu_sum_cif([12, 33, 42], 10) == []


def patrat_perfect(nr):
    """
    functia verifica daca un nummar este patrat perfect
    :param nr: un nuar natural
    :return: True, daca nr e patrat perfect sau False in caz contrar
    """
    for i in range(0, nr + 1):
        if i ** 2 == nr:
            return True
        elif i ** 2 > nr:
            return False


def test_patrat_perfect():
    assert patrat_perfect(4) is True
    assert patrat_perfect(10) is False
    assert patrat_perfect(25) is True


def lista_patrate_perfecte(numar):
    """
    functia determina o lista cu patratele perfecte mmai mici decat un numar
    :param numar: un nummar natural
    :return: lista cu patratele perfecte mmai mici decat numar
    """
    rezultat = []
    for i in range(1, numar + 1):
        if i ** 2 < numar:
            rezultat.append(i ** 2)
        else:
            break
    return rezultat


def test_lista_patrate_perfecte():
    assert lista_patrate_perfecte(10) == [1, 4, 9]
    assert lista_patrate_perfecte(25) == [1, 4, 9, 16]
    assert lista_patrate_perfecte(1) == []


def inlocuire_lista(lista):
    """
    functia cauzeaza afișarea listei obținute din lista inițială în care numerele pătrat perfect sunt înlocuite
    cu radicalul acestora. În cazul numerelor care nu sunt pătrat perfect, acestea sunt înlocuite
    cu o listă cu numerele pătrat perfect mai mici decât numărul inițial.
    Modificările se aplică doar pe numerele pozitive
    :param lista: o lista de nummere intregi
    :return: lista obținuta din lista inițială în care numerele pătrat perfect sunt înlocuite
    cu radicalul acestora. În cazul numerelor care nu sunt pătrat perfect, acestea sunt înlocuite
    cu o listă cu numerele pătrat perfect mai mici decât numărul inițial.
    """
    rezultat = []
    for i in range(0, len(lista)):
        if lista[i] > 0:
            if patrat_perfect(lista[i]) is True:
                rezultat.append(lista[i] ** 0.5)
            else:
                rezultat.append(lista_patrate_perfecte(lista[i]))
        else:
            rezultat.append(lista[i])
    return rezultat


def test_inlocuire_lista():
    assert inlocuire_lista([-5, 4, 10, -3]) == [-5, 2, [1, 4, 9], -3]
    assert inlocuire_lista([-5, -4, -3]) == [-5, -4, -3]
    assert inlocuire_lista([4, 20, -16]) == [2, [1, 4, 9, 16], -16]


def concatenare_nr_poz(lista):
    """
    functia concateneaza numerele pozitive din lista
    :param lista: o lista de numere intregi
    :return: numarul obtinut prin concatenarea numerelor pozitive din lista
    """
    rezultat = ""
    for i in lista:
        if i > 0:
            rezultat = rezultat + str(i)
    return int(rezultat)


def test_concatenare_nr_poz():
    assert concatenare_nr_poz([1, -2, 3]) == 13
    assert concatenare_nr_poz([12, -2, 35]) == 1235
    assert concatenare_nr_poz([-1, -2, 3]) == 3


def main():
    test_cel_mai_mic()
    test_cel_mai_mare()
    test_suma_dintre_cel_mai_mare_nr_si_cel_mai_mic_nr()
    test_suma_cifrelor()
    test_afisare_nr_cu_sum_cif()
    afisare_meniu()
    test_patrat_perfect()
    test_lista_patrate_perfecte()
    test_inlocuire_lista()
    test_concatenare_nr_poz()
    while True:
        optiune = int(input("Dati optiune: "))
        if optiune == 1:
            lista = citire_lista()
        elif optiune == 2:
            print(concatenare_nr_poz(lista))
        elif optiune == 3:
            print(suma_dintre_cel_mai_mare_nr_si_cel_mai_mic_nr(lista))
        elif optiune == 4:
            n = int(input("Dati n: "))
            print(afisare_nr_cu_sum_cif(lista, n))
        elif optiune == 5:
            print(inlocuire_lista(lista))
        elif optiune == 0:
            break
        else:
            print("Optiune gresita! Mai incercati")


main()
