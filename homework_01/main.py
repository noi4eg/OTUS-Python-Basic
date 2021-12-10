"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

    return [number ** 2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num):
    k = 0
    if (num == 0) or (num == 1):
        return False
    for i in range (2, (num // 2) + 1):
        if num % i == 0:
            k += 1
            print (i)
    if k == 0:
        return True
    else:
        return False

def filter_numbers(*args):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """   
    if args[1] == "odd":
        return [arg for arg in args[0] if 1 == arg % 2]

    if args[1] == "even":
        return [arg for arg in args[0] if 0 == arg % 2]

    if args[1] == "prime":
        # return [arg for arg in args[0] if is_prime(arg)]
        return list(filter(lambda i: is_prime(i), args[0]))

