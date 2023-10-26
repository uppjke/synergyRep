#Задание №2
#Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».
#Для решения задачи создайте переменную и в неё положите слово с помощью input()
#А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False

word = input("Введите слово: ")
vowels_chars = {'a': False, 'e': False, 'i': False, 'o': False, 'u': False}
consonants_chars = 0

for char in word:
  if char.lower() in vowels_chars.keys():
    vowels_chars[char] += 1
  elif char.isalpha():
    consonants_chars += 1

print("Количество гласных букв:", sum(vowels_chars.values()))
print("Количество согласных букв:", consonants_chars)
for key in vowels_chars.keys():
  print(f"Количество букв {key}: {vowels_chars[key]}")
