def gen_1(str_):
    """
    :param str_: Предложение, из которого нужно возвращать слова
    :return: Слова из предложения
    """
    for word in str_.split():
        yield word


def count(start, step):
    """
    Бесконечная арифметическая прогрессия

    Функция-генератор умеет принимать новый стартовый элемент, и возвращать новые значения без повторной инициализации

    :param start: Стартовый элемент на момент инициализации
    :param step: Шаг арифметической прогрессии
    :return: Текущий элемент арифметической прогресии
    """
    current_value = start  # текущее значение
    while True:
        new_start = yield current_value  # возвращаем текущий элемент и принимаем новое стартовое значение
        if new_start is None:  # если приняли None, значит вызывался next() и ведем себя как генератор
            current_value += step
        else:  # Если прислали что-то отличное от None, значит это новый элемент и нужно перезапустить прогрессию
            current_value = new_start


def my_random(x0, a, m, c):
    """
    X_n_1 = (a * X_n + c) % m

    :param x0: seed - начальное значение или посевное
    :param a:
    :param m:
    :param c:
    :return:
    """
    if not m > 0:
        raise ValueError('m must be > 0')
    if not 0 < a < m:
        raise ValueError(f'a must be 0 < a < {m}')
    if not 0 < c < m:
        raise ValueError(f'a must be 0 < c < {m}')
    if not x0 < m:
        raise ValueError(f' x0 must be < {m}')

    nums = [x0, a, m, c]
    if not all(map(lambda n: isinstance(n, int), nums)):
        raise TypeError(f'All args must be integer. '
                        f'{list(filter(lambda n: not isinstance(n, int), nums))} not integer')

    # ToDo Реализовать генератор случайных чисел


if __name__ == '__main__':
    # words = "один два шесть восемь"
    # iter_word = gen_1(words)
    #
    # for _ in range(100):
    #     print(next(iter_word))

    count_iter = count(17, 2)
    for _ in range(3):
        print(count_iter.send(None))

    print('-' * 5)
    print(count_iter.send(100))
    print('-' * 5)

    for _ in range(3):
        print(count_iter.send(None))



