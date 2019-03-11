from datetime import datetime
import os
current_path = os.path.dirname(os.path.abspath(__file__))


def logger(path):
    def decorator_logger(function_to_log):
        start_time = datetime.now()
        def new_foo(*args, **kwargs):
            with open(os.path.join(path, 'logs.txt'), 'a', encoding='utf8') as f:
                foo_name = function_to_log.__name__
                foo_return = function_to_log(*args, **kwargs)
                f.write(f"{start_time} FUNCTION {foo_name} RETURNED {foo_return}\n")
            return foo_return
        return new_foo
    return decorator_logger


#Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень внимателен чтобы не потерять ни один документ. Каталог документов хранится в следующем виде:

documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
#Перечень полок, на которых находятся документы хранится в следующем виде:

directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}

@logger(current_path)
def owners_name(number, docs): #имя владельца
  for document in docs:
    if number == document['number']:
      return document['name']
  return 'Ошибка! Такого документа нет'


@logger(current_path)
def all_documents(docs): #все документы
  for document in docs:
    print(f'{document["type"]}: "{document["number"]}" "{document["name"]}"')


@logger(current_path)
def shelf_number(number, shelfs): #номер полки
  for document in shelfs:
    if number in shelfs[document]:
      return document
  return 'Ошибка! Такого документа нет'
  

@logger(current_path)
def create_document(number, docs): #создание нового документа
  new_card = dict()
  new_card["type"] = input('Введите тип документа: ')
  new_card["number"] = number
  new_card["name"] = input('Введите имя: ')
  docs.append(new_card)


@logger(current_path)
def new_directory(number_directory, directories): #проверка директории
  if number_directory not in directories:
    print('Ошибка! Такой директории не существует')
    return False


@logger(current_path)
def add_to_directories(number_directory, number, directs): #
  for directory in directs:
    if number_directory == directory:
      directs[directory].append(number)


@logger(current_path)
def add_document(number_directory, number, docs, directs):
  if new_directory(number_directory, directs) is False:
    return
  add_to_directories(number_directory, number, directs)
  create_document(number,docs)
  print('Документ добавлен')

#Задание к лекции 2.3
@logger(current_path)
def all_names(docs):
  try:
    for document in docs:
      print(f'{document["name"]}')
  except KeyError:
    print('Нет такого ключа!')


@logger(current_path)
def main_interface():
  number_document = lambda: input('Введите номер документа: ')
  number_directory = lambda: input('Введите номер директории для сохранения документа: ')
  print('''
  | ============================
  |  p  -  вывести имя  владельца;
  |  l  -  вывести список всех документов;
  |  s  -  вывести номер полки, на которой лежит документ;
  |  a  -  добавить новый документ;
  |  n  -  вывести имена всех владельцев документов;
  | ============================
  ''')
  while True:
    operation = input('Введите команду: ').lower()
    if operation == 'p':
      print(owners_name(number_document(), documents))
    elif operation == 'l':
      all_documents(documents)
    elif operation == 's':
      print(shelf_number(number_document(),directories))
    elif operation == 'a':
      add_document(number_directory(), number_document(), documents, directories)
    #Задание к лекции 2.3
    elif operation == 'n':
      all_names(documents)

main_interface()
