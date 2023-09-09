import logging
from random import randint

FORMAT = '{levelname} - {asctime} {message} '
logging.basicConfig(filename='employee.log', level=logging.INFO, encoding='utf-8' , format= FORMAT , style='{' )

class Person:
    def __init__(self, last_name, first_name, age):
        self._last_name, self._first_name, self.__age = last_name, first_name, age

    def get_birthday(self):
        return self.__age

    def add_birthday(self):
        self.__age += 1

    def get_fullname(self):
        return f'{self._last_name}, {self._first_name}'

class Employee(Person):
    def __init__(self, *args):
        super().__init__(*args)
        self.__id = randint(10 ** 5, 10 ** 6)
        self.__level = sum(int(i) for i in str(self.__id)) % 7

    def get_id(self):
        return self.__id

    def get_level(self):
        return self.__level

if __name__ == "__main__":
    try:
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        age = int(input("Введите возраст: "))

        if age < 0:
            raise ValueError("Возраст должен быть положительным числом.")

        employee = Employee(last_name, first_name, age)

        logging.info(f"Создан новый сотрудник: {employee.get_fullname()}, ID: {employee.get_id()}, Level: {employee.get_level()}")

        print(employee.get_birthday())
        employee.add_birthday()

        logging.info(f"Информация о сотруднике после добавления дня рождения: ФИО: {employee.get_fullname()}, ID: {employee.get_id()}, Level: {employee.get_level()}, Возраст: {employee.get_birthday()}")

        print(employee.get_fullname())
        print(employee._last_name)
        print(employee.get_birthday())
        print(employee.get_id())
        print(employee.get_level())

    except ValueError as e:
        logging.error(f"Ошибка при вводе данных: {str(e)}")

        print("Произошла ошибка:", str(e))