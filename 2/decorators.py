import time


def decorator(fn):

    def wrapper(*args, **kwargs):
        # до вызова функции

        result = fn(*args, **kwargs)

        # после вызова функции

        return result

    return wrapper


def counter(fn):
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)
        wrapper.count += 1
        print(f'Функция "{fn.__name__}" вызывалась {wrapper.count} раз')

    wrapper.count = 0

    return wrapper


def counter_main():
    @counter
    def my_print():
        print('Hello World')

    for _ in range(5):
        my_print()

    print(my_print.__dict__)  # словарь


import time


def time_(fn):
    """
    Декоратор замеряющий время выполнения любой функции

    :param fn: Функция для замера времени
    :return: Задекорированная функция
    """
    def wrapper(*args, **kwargs):
        t0 = time.time()  # время начала выполнения функции
        result = fn(*args, **kwargs)
        dt = time.time() - t0

        print(f"Время выполнения функции {fn.__name__}: {dt:.10f}")
        return result
    return wrapper


def time_main():
    @time_
    def pow_2(i):
        return 2 ** i

    for i in range(10):
        print(pow_2(i))


def cache(fn):
    def wrapper(*args):
        # по ключу храним аргументы вызова, по значению результат
        dict_cache = wrapper.__dict__
        print(f'Текущее значение кеша: {dict_cache}')

        if args not in dict_cache:
            # считаем значение, запоминаем в кеше и возвращаем результат
            result = fn(*args)
            dict_cache[args] = result
            print(f'Новый результат в кеш {args}:{result}')

        # возвращаем из кеша
        print(f'Результат из кеша')
        return dict_cache[args]

    return wrapper


def cache_main():
    @cache
    def mul(a, b):
        return a * b

    for i in range(1, 5):
        print(f"{i} * {i}")
        mul(i, i)
        print('-----')
        mul(i, i)


def timeit_(count=1):
    def time_decorator(fn):
        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(count):
                t0 = time.time()  # время начала выполнения функции
                result = fn(*args, **kwargs)
                dt = time.time() - t0
                total_time += dt  # общее количесто времени выполния всех функций

            print(f"Время выполнения функции {fn.__name__}: {total_time:.10f}")

            wrapper.dt = total_time / count

            return None

        return wrapper
    return time_decorator


def timeit_main():
    @timeit_(50)
    def mul(*args):
        p = 1
        for value in args:
            p *= value
        return p

    for i in range(1, 10):
        mul(range(i, i+1))
        print(f'Время выполнения для аргументов {list(range(1, i+1))} равно: {mul.dt:.10f}')


if __name__ == '__main__':
    # counter_main()
    # time_main()
    # cache_main()
    timeit_main()
