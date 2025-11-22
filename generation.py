import random

from faker import Faker

from data import DEPARTMENT

faker = Faker()

class Generation:

    @staticmethod
    def user_name():
        user_name = faker.user_name()
        return user_name

    @staticmethod
    def email():
        email = faker.email()
        return email

    @staticmethod
    def address():
        address = faker.street_address()
        return address

    @staticmethod
    def text_box_input():
        user_name = Generation.user_name()
        email = Generation.email()
        current_address = Generation.address()
        permanent_address = Generation.address()

        return user_name, email, current_address, permanent_address

    @staticmethod
    def first_name():
        first_name = faker.first_name()
        return first_name

    @staticmethod
    def last_name():
        last_name = faker.last_name()
        return last_name

    @staticmethod
    def age():
        age = random.randint(18, 65)
        return str(age)

    @staticmethod
    def salary():
        salary = random.randint(500, 20000)
        return str(salary)

    @staticmethod
    def department():
        return random.choice(DEPARTMENT)

print(Generation.department())