#Во входную строку водится последовательность чисел через пробел. 
#Для каждого числа выведите слово ”YES” (в отдельной строке), 
#если это число ранее встречалось в последовательности или ”NO”, если не встречалось.

def check_duplicates(sequence):
    seen = set()
    for num in sequence.split():
        if num in seen:
            print("YES")
        else:
            print("NO")
            seen.add(num)

check_duplicates(input("Введите последовательность чисел: "))
