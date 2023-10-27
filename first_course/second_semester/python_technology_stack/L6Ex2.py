#Задание №2
#Вводится натуральное число X. 
#Подсчитайте количество натуральных делителей числа X (включая 1 и само число). x ≤ 2e9 (2 миллиарда)

def count_divisors(x):
  if x >= 2e9 or x <= 0:
    return 0
  else:
    count = 0
    for i in range(1, x+1):
      if x % i == 0:
        count += 1
    return count

x = int(input("Введите число: "))

if count_divisors(x):
  print(f"Количество натуральных делителей числа {x}: {count_divisors(x)}")
else:
  print("Ошибка:\nлибо введенное число не является натуральным,\nлибо оно больше 2e9")
