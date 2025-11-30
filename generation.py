import random
from calendar import month
from typing import Any

from faker import Faker

from data import DEPARTMENT, SUBJECTS_LIST, STATE_AND_CITY, AutoCompleteData, SelectMenuData

faker = Faker()

class Generation:

    @staticmethod
    def user_name() -> str:
        user_name = faker.user_name()
        return user_name

    @staticmethod
    def email() -> str:
        email = faker.email()
        return email

    @staticmethod
    def address() -> str:
        address = faker.street_address()
        return address

    @staticmethod
    def text() -> str:
        text = faker.text(10)
        return text

    @staticmethod
    def text_box_input():
        user_name: str = Generation.user_name()
        email: str = Generation.email()
        current_address: str = Generation.address()
        permanent_address: str = Generation.address()

        return user_name, email, current_address, permanent_address

    @staticmethod
    def first_name() -> str:
        first_name = faker.first_name()
        return first_name

    @staticmethod
    def last_name() -> str:
        last_name = faker.last_name()
        return last_name

    @staticmethod
    def age() -> str:
        age = random.randint(18, 65)
        return str(age)

    @staticmethod
    def salary() -> str:
        salary = random.randint(500, 20000)
        return str(salary)

    @staticmethod
    def department() -> str:
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
    def date_of_birth() -> str:
        date_of_birth = faker.date_of_birth()
        formatted_date = date_of_birth.strftime("%d %B,%Y")
        return str(formatted_date)

    @staticmethod
    def date():
        date = faker.date(pattern="%m/%d/%Y")
        return date

    @staticmethod
    def subjects():
        num = random.randint(1,14)
        subject_choice = random.sample(SUBJECTS_LIST, num)
        return subject_choice

    @staticmethod
    def state_and_city() -> tuple[Any, Any]:
        state = random.choice(list(STATE_AND_CITY.keys()))
        city = random.choice(STATE_AND_CITY[state])
        return state, city

    @staticmethod
    def color():
        color = random.choice(AutoCompleteData.COLORS)
        return color

    @staticmethod
    def date_and_time():
        month_random = faker.month_name()
        day_random = str(int(faker.day_of_month()))
        year_random = faker.year()
        time_random = faker.date_time_between().strftime("%I:%M %p").lstrip("0")
        date_and_time = f"{month_random} {day_random}, {year_random} {time_random}"
        return date_and_time

    @staticmethod
    def color_for_old_menu():
        color = random.choice(SelectMenuData.OLD_STYLE_SELECT_MENU_OPTIONS)
        return color

    @staticmethod
    def colors_for_multiselect_drop_down():
        colors = SelectMenuData.MULTISELECT_DROP_DOWN_OPTIONS
        num = random.randint(1, len(colors))
        colors_choice = random.sample(colors, num)
        return colors_choice

    @staticmethod
    def cars_for_standard_select_menu():
        cars = SelectMenuData.STANDARD_MULTI_SELECT_OPTIONS
        num = random.randint(1, len(cars))
        cars_choices = random.sample(cars, num)
        return cars_choices

    @staticmethod
    def selecting_random_elements(elements):
        quantity = random.randint(1, len(elements))
        selected_elements  = random.sample(elements, quantity)
        return selected_elements