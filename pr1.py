import random

numbers = [random.randint(-100, 100) for _ in range(random.randint(1, 20))]

sum_1 = 0
sum_2 = 0
sum_3 = 0
sum_4 = 1
sum_5 = 1
sum_6 = 0

min_num = float('inf')
max_num = float('-inf')

first = None
last = None

for i, num in enumerate(numbers):
    if num < 0:
        sum_1 += num

    if num % 2 == 0:
        sum_2 += num
    else:
        sum_3 += num
    if i % 3 == 0:
        sum_4 *= num
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

    if num > 0:
        if first is None:
            first = num
        last = None

        if last is not None:
            sum_6 += num


print("Список чисел:", numbers)
print("Сумма отрицательных чисел:", sum_1)
print("Сумма четных чисел", sum_2)
print("Сумма нечетных чисел:", sum_3)
print("Произведение с элементами с индексами кратными трем:", sum_4)
print("Произведение между минимальным и максимаьлным элементом:", sum_5)
print("Сумма между первым и последним:", sum_6)
