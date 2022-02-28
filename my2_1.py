"""
9. Мастям гральних карт присвоєно порядкові номери: 1 - піки, 2 - трефи, 3 - бубни, 4 - черви.
Вартості карт, які старші за десятку, привласнені номери: 11 - валет, 12 - дама, 13 - король,
14 - туз. Дано два цілих числа: N - вартість (6<=N<=14) і M - масть карти (1<=M<=4). Вивести
назву відповідної карти виду <<шістка бубон>>, <<дама черв>>, <<туз треф>>.
"""


def found_value(value):
    """ Функция расчета достоинства карты по номеру """
    if value == 6:
        v = "шестерка"
        return v
    elif value == 7:
        v = "семерка"
        return v
    elif value == 8:
        v = "восьмерка"
        return v
    elif value == 9:
        v = "девятка"
        return v
    elif value == 10:
        v = "десятка"
        return v
    elif value == 11:
        v = "валет"
        return v
    elif value == 12:
        v = "дама"
        return v
    elif value == 13:
        v = "кароль"
        return v
    elif value == 14:
        v = "туз"
        return v
    else:
        return print("Достоинства под номером ", value, " не существует!")


def found_suit(suit):
    """ Функция расчета масти карты по номеру """
    if suit == 1:
        s = "пик"
        return s
    elif suit == 2:
        s = "треф"
        return s
    elif suit == 3:
        s = "бубен"
        return s
    elif suit == 4:
        s = "черв"
        return s
    else:
        return print("Масти под номером ", suit, " не существует!")


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
            x = "Даная карта - " + found_value(n) + " " + found_suit(m)
            print(x)
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
