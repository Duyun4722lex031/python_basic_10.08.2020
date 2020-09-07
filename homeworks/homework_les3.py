# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_division(number_one: float, number_two: float) -> float:
    return  number_one / number_two

if __name__ == '__main__':
    try:
        print(my_division(int(input('введите первое число')),
                          int(input('введите второе число'))))
    except ZeroDivisionError:
        print('деление на ноль недопустимо')