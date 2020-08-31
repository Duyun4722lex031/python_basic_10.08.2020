# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def inform(surname, birthday, city, email, phone_number):
    print(surname, birthday, city, email, phone_number)

if __name__ == '__main__':
    inform(birthday = input('введитк день рождения'),
           surname = input('введите фамилию'),
           city = input('введите город'),
           email = input('введите электронный адрес'),
           phone_number = input('ведите номер телефона'))