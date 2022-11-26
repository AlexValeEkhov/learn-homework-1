"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {'Как тебя зовут?': 'Пайтон',
  'Как дела?': 'Хорошо!',
  'Что делаешь?': 'Программирую',
  'Что бы еще спросить?': 'Не знаю..',
  'Как мне выйти?': 'Выходи. Пока.'}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    while True:
      user_question = input('Задай вопрос: ')
      if user_question == 'Как мне выйти?':
          print(questions_and_answers['Как мне выйти?'])
          break
      for question in questions_and_answers:
        
        if user_question == question:
          print(questions_and_answers[question])
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
