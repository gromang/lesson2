"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    """
    Замените pass на ваш код
    """
    good = False
    while not good:
        ask = input('Как дела?')
        if ask == 'Хорошо':
            good = True
        else:
            good = False


if __name__ == "__main__":
    ask_user()
