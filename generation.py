import random

from faker import Faker

from data import DEPARTMENT, SUBJECTS_LIST

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

    @staticmethod
    def text_file():
        file_name = f"file_upload{random.randint(1,100)}.txt"
        file_path = rf"C:\Users\adizerko\Downloads\{file_name}"
        text = faker.text(100)
        with open(file_path, "w") as f:
            f.write(text)

        return file_name, file_path
    @staticmethod
    def gender_forms():
        num = random.randint(1,3)
        gender = ""
        if num == 1:
            gender = "Male"
        elif num == 2:
            gender = "Female"
        else:
            gender = "Other"

        return gender, num

    @staticmethod
    def phone_number():
        phone = random.randint(1000000000, 9999999999)
        return phone

    @staticmethod
    def date_of_birth():
        date_of_birth = faker.date_of_birth()
        return str(date_of_birth)

    @staticmethod
    def subjects():
        num = random.randint(1,14)
        subject_choice = random.sample(SUBJECTS_LIST, num)
        return subject_choice

    @staticmethod
    def hobbies():
        num = random.randint(1,3)




print(Generation.date_of_birth())