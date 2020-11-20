from math import sqrt
from operator import add


def get_dist(point): return (point[0] ** 2 + point[1] ** 2) ** 0.5  # ToDo: Change to lambda function


def map_1():
    """
    Дан список точек, найти самую удаленную
    точку от начала координат
    """
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    # iter_dist = map(get_dist, pts)
    # list_dist = list(iter_dist)
    # print(list_dist)
    # max_dist = max(list_dist)
    # print(max_dist)

    print(max(map(get_dist, pts)))


def map_2():
    """
    Дан список чисел в различных форматах, привести их к типу int
    """
    num_list = [
        "12",
        "14",
        3.1415926,
        5,
        0xFF,
        0b1010101010
    ]

    print(list(map(int, num_list)))


def _round(a, n=2): return round(a, n)  # ToDo: Change to lambda function


def map_3():
    """
    Дан список чисел округлить их до 2 знаков после запятой
    """
    my_floats = [
        4.356345,
        6.0934,
        3.245235,
        9.77545,
        2.164234234,
        8.884234235,
        4.595235346645
    ]

    print(list(map(_round, my_floats)))
    print(list(map(round, my_floats, [2] * len(my_floats))))


def map_4():
    """
    Найти длину самого длинного слова
    """
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    print(max(map(len, list_words)))


def map_5():
    """
    Перевести все слова в верхний регистр

    "test".upper()
    str.upper("test")
    """
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    print(list(map(str.upper, list_words)))


def _add(a, b): return a + b  # ToDo: Change to lambda function


def map_6():
    """
    Поэлементно сложить два списка
    [1, 2, 3] + [4, 5, 6] == [5, 7, 9]
    """

    print(list(map(_add, [1, 2, 3], [4, 5])))
    print(list(map(add, [1, 2, 3], [4, 5, 6])))


def map_7():
    """
    1. Найти длину всех последовательностей
    2. Найти общее количество элементов в списке
    3. Найти размер максимальной последовательности
    """

    a = [
        [2, 3, 5, 7],
        [11, 13, 17, 19],
        [23, 29],
        [31, 37]
    ]

    # print(list(map(len, a)))  # 1
    # print(sum(map(len, a)))  # 2
    # print(max(map(len, a)))  # 3

    len_a_list = list(map(len, a))
    print(len_a_list)  # 1
    print(sum(len_a_list))  # 2
    print(max(len_a_list))  # 3


def debug():
    print("1")
    print("2")
    print("3")
    print("4")


def foor_loop():
    int('12gh')
    for i in range(-100, 100):
        print(1000 / i)


def parse_matrix():
    matrix = """
        1 2 3
        4 5 6
        7 8 9
        10 11 12
    """
    matrix = matrix.strip()
    matrix = matrix.split('\n')
    matrix = list(map(str.strip, matrix))
    matrix = list(map(str.split, matrix))
    matrix = [list(map(int, sublist)) for sublist in matrix]


    print(matrix)


if __name__ == '__main__':
    # map_1()
    # map_2()
    # map_3()
    # map_4()
    # map_5()
    # map_6()
    # map_7()
    # filter_3()
    # print('0')
    # debug()
    # print('100')
    #
    # print("1000")
    # foor_loop()
    parse_matrix()