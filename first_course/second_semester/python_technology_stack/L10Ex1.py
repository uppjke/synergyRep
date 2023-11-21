#Ранее вы выполняли задание связанное с ветеринарной клиникой. 
#В той задаче вам предстояло вывести информацию о питомце на экран. Сейчас вам необходимо создать словарь pets = {}
#Примерный вид будет следующим:
#pets = {
#  "Имя питомца": {
#    'Вид питомца': # придумайте каким образом сюда внести информацию,
#    'Возраст питомца': # придумайте каким образом сюда внести информацию,
#    'Имя владельца': # придумайте каким образом сюда внести информацию
#  }
#}
#У вас должен получиться словарь, с ещё одним словарём внутри. 
#То есть, есть словарь pets. Он в себе хранит ещё один словарь, который обозначается именем питомца. 
#Имя питомца также нужно каким-то образом вносить туда.
#Задача не будет считаться выполненной, если вы заходите сразу внести информацию, не прибегая в функции input()
#Например:
#pets = {
#  "Мухтар": {
#    "Вид питомца": "Собака",
#    "Возраст питомца": 9,
#    "Имя владельца": "Павел"
#  }
#}
#Так должен будет выглядеть результируюший словарь, но первоначальный его вид - пустой. 
#Его необходимо заполнить пользовательским вводом через консоль с помощью функции input(), а не вписать значения уже в самом коде.
#Возраст питомца должен быть типа int Всё остальное - строки
#Так как возраст питомца указывается типом int. Необходимо, в соответствии с указанным возрастом выводит год, года или лет. Например:
#Его возраст: 24 года
#Его возраст: 21 год
#Его возраст: 19 лет
#И теперь осталось только получить всю информацию о питомце в виде строки, как из задания по Урок №3. 
#Ввод-вывод и базовые переменные. Задание №1, но с небольшими изменениями. 
#Для получения информации необходимо воспользоваться методами словаря keys() и values(): 
#Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша

pets = {}

pet_name = input("Введите имя питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
pet_owner = input("Введите имя владельца: ")

pets[pet_name] = {
    "Вид питомца": pet_type,
    "Возраст питомца": pet_age,
    "Имя владельца": pet_owner
}

if pet_age % 10 == 1 and pet_age % 100 != 11:
  age_description = "год"
elif 2 <= pet_age % 10 <= 4 and (pet_age % 100 < 10 or pet_age % 100 >= 20):
  age_description = "года"
else:
  age_description = "лет"

info_str = f"Это {pet_type.lower()} по кличке \"{pet_name}\". Возраст питомца: {pet_age} {age_description}. Имя владельца: {pet_owner}"
print(info_str)