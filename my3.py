"""
14. Дано три різних числа. Знайти, яке з них є середнім (більше одного, але м енше іншого).
"""


def check(num1, num2, num3):
    """ Функция пасчета среднего числа среди трех разных чисел """
    if num2 < num1 < num3 or num3 < num1 < num2:
        return num1
    elif num2 < num3 < num1 or num1 < num3 < num2:
        return num3
    elif num1 < num2 < num3 or num3 < num2 < num1:
        return num2
    else:
        s = "Числа должны быть разными!"
        return s


def main():
    print(" Добро пожаловать в программу расчета среднего числа между тремя!")
    choice = None
    while choice != "0":
        print(
            """
            0 - Выйти
            1 - Найти среднее число между тремя 
            """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    a = float(input("Введите первое число "))
                    break
                except ValueError:
                    print("Несоответствие типов!")
            while True:
                try:
                    b = float(input("Введите второе число "))
                    break
                except ValueError:
                    print("Несоответствие типов!")
            while True:
                try:
                    c = float(input("Введите третье число "))
                    break
                except ValueError:
                    print("Несоответствие типов!")
            print(check(a, b, c))
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()