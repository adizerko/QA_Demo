from faker.generator import random

from data import CHECKBOX_ELEMENTS


class Helper:

    @staticmethod
    def help_random():
        check_box_element = random.choice(CHECKBOX_ELEMENTS)
        return check_box_element

