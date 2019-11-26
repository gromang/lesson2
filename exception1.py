"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


def ask_user():
    """
    Замените pass на ваш код
    """
    def ask_user_dict(ask):
        dictionary = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую",
                      "Сколько тебе лет?": "34", "Как тебя зовут?": "Роман"}
        ask = ask.lstrip()
        answer = dictionary.get(ask, "Я не знаю что ответить")
        return answer

    print('Задайте Ваш вопрос\n')

    while True:
        try:
            ask = input('Пользователь:')
            print(f'Программа: {ask_user_dict(ask)}')
        except KeyboardInterrupt:
            print('Пока!')
            break


if __name__ == "__main__":
    ask_user()
