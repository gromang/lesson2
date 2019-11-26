"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    all_scores = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
                  {'school_class': '5b', 'scores': [2, 2, 5, 3, 4]},
                  {'school_class': '7g', 'scores': [5, 5, 4, 5, 3]},
                  {'school_class': '9a', 'scores': [2, 4, 4, 2, 5]}]

    i = 0
    school_mid = 0

    for classes in all_scores:
        class_mid = 0
        class_mid = sum(classes['scores'])/len(classes['scores'])
        school_mid += class_mid
        i += 1

        print(f'Средняя оценка по классу {classes['school_class']}  : {class_mid}')

    school_mid = round(school_mid / i, 1)

    print(f'Средняя оценка по школе      : {school_mid}')


if __name__ == "__main__":
    main()
