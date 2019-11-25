"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    #str1 = input('Введите первую строку: ')
    #str2 = input('Введите вторую строку: ')

    def compare(str1, str2):
        if not str1 or not str2 or not isinstance(str1, str) or not isinstance(str2, str):
            return 0
        elif str1 == str2:
            return 1
        elif len(str1) > len(str2):
            return 2
        elif str2 == 'learn':
            return 3
        else:
            return

    print(compare('', ''))
    print(compare('', 4))
    print(compare(99, 4))
    print(compare(6, 'learn'))
    print(compare('learn', 'learn'))
    print(compare('learning python', 'learning'))
    print(compare('study', 'learn'))
    print(compare('learn', 'learning'))


if __name__ == "__main__":
    main()
