#Задание №2
#Дана строка, длина которой не превосходит 1000. 
#Вам требуется преобразовать все идущие подряд пробелы в один. 
#Выведите измененную строку.

def consolidate_spaces(string):
    return ' '.join(string.split())

s = input("Введите строку: ")

if(len(s) > 1000):
  print("Ошибка: длина строки больше тысячи символов!")
else:
  print(consolidate_spaces(s))
