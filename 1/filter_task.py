from operator import add, getitem
from itertools import repeat
from itertools import count, zip_longest
import random


def check_even(n): return n % 2 == 0  # ToDo: Change to lambda function


def pow_2(n): return n ** 2  # ToDo: Change to lambda function


def filter_1():
    """
    Квадраты всех четных натуральных чисел (используя map и filter)
    """
    n = 10
    all_numbers = count(1, 1)
    all_even_numbers = filter(check_even, all_numbers)
    all_even_numbers_pow_2 = map(pow_2, all_even_numbers)

    for _ in range(n):
        print(next(all_even_numbers_pow_2))

    print(f'Первые {n} получены')

    for _ in range(n):
        print(next(all_even_numbers_pow_2))

    print(f'Вторые {n} получены')

    # map(pow_2, filter(check_even, all_numbers))


def check_neg_and_3(n): return (n < 0) and (n % 3 == 0)  # ToDo: Change to lambda function


def filter_2():
    """
    Найти все отрицательные числа кратные 3
    """
    n = 100
    random_list = [random.randint(-100, 100) for _ in range(n)]

    print(list(filter(check_neg_and_3, random_list)))


def get_char(i, str_="Всем привет"): return str_[i]  # ToDo: Change to lambda function


def filter_3():
    """
    «Всем привет», [1, 3, 5] -> «смп»
    """

    s = "Всем привет"
    index_list = [1, 3, 5]
    print("".join(map(getitem,
                      repeat(s, len(index_list)), index_list)))

    """
    getitem(s, i) == s[i]
    index_list = [1, 3, 5]
    str_list = ["Всем привет", "Всем привет", "Всем привет"]
    ("Всем привет", 1) -> c
    ("Всем привет", 3) -> м
    ("Всем привет", 5) -> п

    """


def zip_1():
    figures = [
        'круг',
        'квадрат',
        'ромб',
        'прямоуольник'
    ]

    colors = [
        'красный',
        'оранжевый',
        'желтый'
    ]
    default_color = 'синий'

    for figure, color in zip(figures, colors):
        print(f"Фигура {figure} окрашена в {color} цвет")

    print('-' * 10)

    for figure, color in zip_longest(figures, colors,
                                     fillvalue=default_color):
        print(f"Фигура {figure} окрашена в {color} цвет")


def enumerate_1():
    str_ = 'Всем привет'
    for i, char in enumerate(str_):
        print(f'Index: {i:>2} | Char: {char}')
    print(list(enumerate(str_)))


def enumerate_2(sequence, start=0):
    return zip(range(start, len(sequence) + start), sequence)


if __name__ == '__main__':
    # filter_1()
    # filter_2()
    # zip_1()
    # enumerate_1()
    a = [3, 2, 1]
    for index, value in enumerate_2(a, 1):
        print(f'Index: {index} | Value: {value}')
