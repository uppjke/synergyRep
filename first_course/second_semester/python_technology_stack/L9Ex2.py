#Вводятся два списка чисел, которые могут содержать до 100000 чисел каждый. 
#Все числа каждого списка находятся на отдельной строке. 
#Выведите, сколько чисел содержится одновременно как в первом списке, так и во втором.

list1 = set(map(int, input().split()))
list2 = set(map(int, input().split()))
result = len(list1.intersection(list2))
print(result)
