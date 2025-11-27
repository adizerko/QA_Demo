from datetime import datetime

from faker.generator import random

from data import CHECKBOX_ELEMENTS


class Helper:

    @staticmethod
    def help_random():
        check_box_element = random.choice(CHECKBOX_ELEMENTS)
        return check_box_element

    @staticmethod
    def formated_time(time_str_24):
        time_obj = datetime.strptime(time_str_24, "%H:%M")
        hour_12 = int(time_obj.strftime("%I"))
        minute = time_obj.strftime("%M")
        am_pm = time_obj.strftime("%p")
        time_12 = f"{hour_12}:{minute} {am_pm}"

        return time_12

