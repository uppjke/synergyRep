#Задание №1
#В первой строке вводится число N. Далее в N строк вводится N чисел (1 ≤ N ≤ 10000), по одному числу на строке. 
#Все числа по модулю не превышают 10e5. Переверните массив чисел. Выведите N чисел - перевернутый массив.

N = int(input("Введите количество чисел: "))
nums = []
for _ in range(N):
    nums.append(int(input()))
  
print()

reversed_nums = nums[::-1]
for num in reversed_nums:
    print(num)