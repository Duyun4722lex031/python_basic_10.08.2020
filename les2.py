my_str = 'HELLO my Dear Friends' # Строки неизменяемый тип данных как и INT FlOAT BOOL

my_list = [1, 2, 3, 'HELLO', True, False, [1, 2, 3]] # Список list() изменяемый тип данных, коллекция

my_tuple = [1, 2, 3, 'HELLO', True, False, [1, 2, 3]] # Кортеж tuple() неизменяемый тип, коллекция

temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
comp = n + int(t1) + int(t2)
print("Результат равен:", comp)


'''for char in reversed(my_str) :
    print(char)

len_obj = len(my_str)

while len_obj:
    len_obj -= 1
    char = my_str[len_obj]
    print(char)


iter_obj = my_str.__iter__()

while True:
    try:
        char = next(iter_obj)
    except StopIteration:
        break
    print(char)'''
