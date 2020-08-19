def some_funk(some_a:float, some_b:float, some_c:int = 1) -> float:
    """Вычисляет сумму и возводит в степень

    :param some_a:float первый аргумент
    :param some_b:float второй аргумент
    :param some_c:int степень
    :return:
    """
    result = (some_a + some_b) ** some_c
    return result

print(some_funk(2, 4))
