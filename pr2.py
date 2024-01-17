import random

numbers = [random.randint(-100, 100) for _ in range(random.randint(1, 20))]
chet = [int(i) for i in numbers if i % 2 == 0]
nech = [int(i) for i in numbers if i % 2 != 0]
minus = [int(i) for i in numbers if i < 0]
plus = [int(i) for i in numbers if i > 0]



print("Список чисел:", numbers)
print("Четные числа:", chet)
print("Нечетные числа:", nech)
print("Отрицательные числа:", minus)
print("Положительные числа:", plus)




