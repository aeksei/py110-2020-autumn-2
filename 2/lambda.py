def lambda_3():
    def maker_add(n):
        def add(x):
            return x + n
        return add

    # maker_add = lambda n: lambda x: x + n

    add_5 = maker_add(5)  # n = 5
    print(add_5(10))  # 15  x = 10
    print(add_5(25))  # 30  x = 25


def lambda_1():
    """
    Создать список, в котором каждый элемент –
    кортеж из двух чисел. Отсортировать данный
    список по убыванию вторых элементов кортежей.
    """
    from operator import itemgetter

    n = 5
    tuple_list = [(n - i, i) for i in range(n)]
    print(tuple_list)

    # itemgetter(1) == lambda item: item[1]

    print(sorted(tuple_list,
                 key=itemgetter(1),
                 reverse=True))


def lambda_2():
    words = "один два шесть восемь"
    list_words = words.split()

    print(sorted(list_words,
                 key=len,  # key=lambda word: len(word),
                 reverse=True))


if __name__ == "__main__":
    # lambda_1()
    lambda_2()
    # lambda_3()
