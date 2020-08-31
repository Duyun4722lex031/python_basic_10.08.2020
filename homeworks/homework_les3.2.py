# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_funk(max_1, max_2, max_3):
    a = [max_1, max_2, max_3]
    minimum_1 = min(a)
    a.remove(minimum_1)
    print(sum(a))


if __name__ == '__main__':
    my_funk(10,20,30)