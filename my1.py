"""
4. Для даного дійсного x знайти значення наступної функції f, що приймає дійсні значення:
f(x) = 2*sin(x), якщо x>0; f(x) = 6-x, якщо x<=0.
"""
import math


def calculation(argument):
    """ Метод расчета аргумента функции """
    if argument > 0:
        function = 2 * math.sin(argument)
    else:
        function = 6 - argument
    return function


def main():
    print(" Добро пожаловать в программу расчета функции!")
    choice = None
    while choice != "0":
        print(
            """
            0 - Выйти
            1 - Найти значение функции
            """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    x = float(input("Введите вещественное число "))
                    break
                except ValueError:
                    print("Несоответствие типов!")
            if x > 0:
                s = "Аргумент функции f(x) = 2*sin(x) равен " + str(calculation(x))
                print(s)
            else:
                s = "Аргумент функции f(x) = 6-x равен " + str(calculation(x))
                print(s)
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
