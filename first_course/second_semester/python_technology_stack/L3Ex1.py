#Задание №1
#Давай представим, что мы пишем бэкенд для сайта ветеринарной клиники. 
#Нам нужно написать программу, которая будет запрашивать у пользователя вид питомца, 
#его возраст и кличку, а потом выведет все эти данные в одно предложение. Например:
#Это желторотый питон по кличке "Каа". Возраст: 34 года.

pet_type = input("Введите вид питомца: ")
age = input("Введите возраст питомца: ")
name = input("Введите кличку питомца: ")

sentence = f'Это {pet_type} по кличке "{name}". Возраст: {age} года.'
print(sentence)
