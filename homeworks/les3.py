def some_funk(some_a:float, some_b:float, some_c:int = 1) -> float:
    """Вычисляет сумму и возводит в степень

    :param some_a:float первый аргумент
    :param some_b:float второй аргумент
    :param some_c:int степень
    :return:
    """
    result = (some_a + some_b) ** some_c
    return result

def my_map(funk, iter_obj):
    result = []
    for itm in iter_obj:
        result.append(funk(itm))
        return result

def my_zip(*args):
    idx = 0
    while True:
        result = []
        idx_2 = 0
        try:
          while True:

        except IndexError:
            break
        yield tuple(result)
        idx += 1



"""Встроенные функции
map,
sorted,
min,
sum,
max,
zip,
enumerate,
range
"""