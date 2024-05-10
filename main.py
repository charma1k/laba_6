"""
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.
Вариант 15. Вывести все четные натуральные числа до n, крайняя левая цифра которых не превышает 5.
"""

import timeit
import itertools

# Алгоритмический подход
def is_valid_alg(number):
    return str(number)[0] in '012345' and number % 2 == 0

def algorithmic_approach(n):
    result = []
    for number in range(2, n, 2):
        if is_valid_alg(number):
            result.append(number)
    return result

# Подход с использованием itertools
def functional_approach_itertools(n):
    result = []
    max_length = len(str(n))
    for length in range(1, max_length):
        for digits in itertools.product('012345', '0123456789' * (length - 1)):
            number = int(''.join(digits))
            if number < n and number % 2 == 0:
                result.append(number)
    for digits in itertools.product('012345', '0123456789' * (max_length - 2)):
        number = int(''.join(digits) + '0')
        if number < n:
            result.append(number)
    return result

# Усложненный алгоритмический подход с дополнительным условием
def complex_algorithmic_approach(n):
    result = []
    for number in range(2, n, 2):
        if is_valid_alg(number) and number % 10 != 0:
            result.append(number)
    return result

# Усложненный подход с использованием itertools и дополнительным условием
def complex_functional_approach_itertools(n):
    result = []
    max_length = len(str(n))
    for length in range(1, max_length):
        for digits in itertools.product('012345', '123456789' * (length - 1)):
            number = int(''.join(digits))
            if number < n and number % 2 == 0:
                result.append(number)
    for digits in itertools.product('012345', '123456789' * (max_length - 2)):
        number = int(''.join(digits) + '0')
        if number < n and number % 10 != 0:
            result.append(number)
    return result

# Сравнение времени выполнения
n = int(input("Введите число n: "))

# Алгоритмический подход
start_time_alg = timeit.default_timer()
algorithmic_result = algorithmic_approach(n)
time_alg = timeit.default_timer() - start_time_alg

# Подход с использованием itertools
start_time_func = timeit.default_timer()
functional_result_itertools = functional_approach_itertools(n)
time_func = timeit.default_timer() - start_time_func

# Усложненный алгоритмический подход
start_time_complex_alg = timeit.default_timer()
complex_algorithmic_result = complex_algorithmic_approach(n)
time_complex_alg = timeit.default_timer() - start_time_complex_alg

# Усложненный подход с использованием itertools
start_time_complex_func = timeit.default_timer()
complex_functional_result_itertools = complex_functional_approach_itertools(n)
time_complex_func = timeit.default_timer() - start_time_complex_func

# Вывод результатов
print("Алгоритмический подход:")
print(algorithmic_result)
print("Время выполнения: {:.6f} секунд".format(time_alg))

print("\Подход с использованием itertools:")
print(functional_result_itertools)
print("Время выполнения: {:.6f} секунд".format(time_func))

print("\nУсложненный алгоритмический подход:")
print(complex_algorithmic_result)
print("Время выполнения: {:.6f} секунд".format(time_complex_alg))

print("\nУсложненный подход с использованием itertools:")
print(complex_functional_result_itertools)
print("Время выполнения: {:.6f} секунд".format(time_complex_func))

# Сравнение результатов
print("\nСравнение времени выполнения:")
print(f"Алгоритмический подход: {time_alg:.6f} сек.")
print(f"Подход с использованием itertools: {time_func:.6f} сек.")
print(f"Усложненный алгоритмический подход: {time_complex_alg:.6f} сек.")
print(f"Усложненный подход с использованием itertools: {time_complex_func:.6f} сек.")
