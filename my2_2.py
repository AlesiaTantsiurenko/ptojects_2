"""
9. Мастям гральних карт присвоєно порядкові номери: 1 - піки, 2 - трефи, 3 - бубни, 4 - черви.
Вартості карт, які старші за десятку, привласнені номери: 11 - валет, 12 - дама, 13 - король,
14 - туз. Дано два цілих числа: N - вартість (6<=N<=14) і M - масть карти (1<=M<=4). Вивести
назву відповідної карти виду <<шістка бубон>>, <<дама черв>>, <<туз треф>>.
"""


def value_dict(vl):
    """ Функция расчета достоинства карты по номеру """
    values = {
        6: "шестерка",
        7: "семерка",
        8: "восьмерка",
        9: "девятка",
        10: "десятка",
        11: "валет",
        12: "дама",
        13: "кароль",
        14: "туз"
    }
    v = values.get(vl, "Карты с таким значением не существует!")
    return v


def suit_dict(st):
    """ Фунуция расчета масти карты по номеру """
    suits = {
        1: "пик",
        2: "треф",
        3: "бубен",
        4: "черв"
    }
    s = suits.get(st, "Карты с такой мастью не существует!")
    return s


def main():
    print(" Добро пожаловать в программу расчета игральной карты!")
    choice = None
    while choice != "0":
        print(
            """
            0 - Выйти
            1 - Найти значение игральной карты
            """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    n = int(input("Введите достоинство карты [6;14] "))
                    if 5 < n < 15:
                        break
                    else:
                        print("Достоинства под номером ", n, " не существует!")
                except ValueError:
                    print("Не соответствие типов!")
            while True:
                try:
                    m = int(input("Введите масть карты [1;4]"))
                    if 0 < m < 5:
                        break
                    else:
                        print("Масти под номером ", m, " не существует!")
                except ValueError:
                    print("Несоответствие типов!")
            x = "Даная карта - " + value_dict(n) + " " + suit_dict(m)
            print(x)
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
